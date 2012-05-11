from re import sub
from os import system
from settings import UPLOAD_DIR, UPLOAD_LOG
from multiprocessing import Process
from django.db import models, connection, close_connection, transaction
from pyPdf import PdfFileReader, PdfFileWriter
from urllib2 import urlopen
from documents.models import Document

import logging
logger = logging.getLogger('das_logger')
hdlr = logging.FileHandler(UPLOAD_LOG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def parse_words(doc, content):
    # split and keep the words
    words = [x.lower() for x in sub(r'\W', ' ', content).split() if len(x) > 2]

    terms_count = dict()
    for word in words:
        terms_count[word] = terms_count.get(word, 0) + 1

    cursor = connection.cursor()
    cursor.execute('select max(id) from search_wordentry;')
    id = cursor.fetchone()[0];
    if not id:
        id = 0

    for word, count in terms_count.iteritems():
        # too slow : 
        # WordEntry.objects.create(word=word, document=doc, count=count)
        id += 1
        cursor.execute("insert into search_wordentry values(%d, '%s', %d, %d);" %
                       (id, word, doc.id, count))
    connection.commit_unless_managed()
    cursor.close()

    return len(words)

@transaction.commit_manually
def process_page(doc, page, num, convert):
    tmp = PdfFileWriter()
    tmp.addPage(page)
    out = file("/tmp/%d_cur.pdf" % doc.pk, 'w')
    tmp.write(out)
    out.close()
    pagename = "%s/doc_%04d_%04d.jpg" % (UPLOAD_DIR, doc.pk, num)
    mininame = "%s/doc_mini_%04d_%04d.jpg" % (UPLOAD_DIR, doc.pk, num)
    w, h = page.bleedBox.getWidth(), page.bleedBox.getHeight()
    if convert:
        system("gm convert -resize %dx%d -quality 90 -density 350 /tmp/%d_cur.pdf %s" %
               (w, h, doc.pk, pagename))
        system("gm convert -resize 118x1000 -quality 90 -density 100 /tmp/%d_cur.pdf %s" % 
               (doc.pk, mininame))
    doc.add_page(num, pagename, mininame, w, h)
    transaction.commit()
    system("rm /tmp/%d_cur.pdf" % doc.pk)

@transaction.commit_manually
def process_file_safe(docid, upfile, convert=True):
    close_connection()
    doc = Document.objects.get(pk=docid)
    logger.info('Starting processing of doc %d (from %s) : %s' % 
                (docid, doc.owner.username, doc.name))
    filename = UPLOAD_DIR + '/' + str(docid) + '.pdf'

    # sauvegarde du document original
    fd = open(filename, 'w')
    fd.write(upfile.read())
    fd.close()

    # sauvegarde du nombre de page
    fd = open(filename, 'r')
    pdf = PdfFileReader(fd)
    doc.set_npages(pdf.numPages)
    transaction.commit()

    # activate the search system
    system("pdftotext " + filename)
    words = open(UPLOAD_DIR + '/' + str(docid) + '.txt', 'r') 
    doc.set_wsize(parse_words(doc, words.read()))
    words.close()
    transaction.commit()

    # iteration page a page, transform en png + get page size
    num = 1
    for page in pdf.pages:
        process_page(doc, page, num, convert)
        num += 1

    fd.close()
    logger.info('End of processing of doc %d' % docid)

@transaction.commit_manually
def process_file(docid, upfile, convert=True):
    try:
        process_file_safe(docid, upfile, convert)

    except Exception as e:
        close_connection()
        doc = Document.objects.get(pk=docid)
        logger.error('process file error for doc %d (from %s) : %s' % 
                     (docid, doc.owner.username, str(e)))
        doc.delete()
        transaction.commit()

@transaction.commit_manually
def download_file(docid, url, convert=True):
    logger.info('Starting download of doc %d : %s' % (docid, url))
    try:
        raw_doc = urlopen(url)

    except Exception as e:
        close_connection()
        doc = Document.objects.get(pk=docid)
        logger.error('download error for doc %d (from %s), url %s : %s' % 
                     (docid, doc.owner.username, url, str(e)))
        doc.delete()
        transaction.commit()

    else:
        process_file(docid, raw_doc, convert)

# convert used for testing purpose
def run_process_file(docid, file, convert=True):
    if convert:
        p = Process(target=process_file, args=(docid, file))
        p.start()
    else:
        process_file(doc, file, False)

# convert used for testing purpose
def run_download_file(docid, url, convert=True):
    if convert:
        p = Process(target=download_file, args=(docid, url, convert))
        p.start()
    else:
        download_file(docid, url, False)
