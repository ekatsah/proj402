from re import sub
from os import system
from settings import UPLOAD_DIR
from multiprocessing import Process
from django.db import models, connection
from pyPdf import PdfFileReader, PdfFileWriter
from urllib2 import urlopen

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
        cursor.execute('insert into search_wordentry values(%d, "%s", %d, %d);' %
                       (id, word, doc.id, count))
    connection.commit_unless_managed()
    cursor.close()

    return len(words)

def process_page(doc, page, num, convert):
    tmp = PdfFileWriter()
    tmp.addPage(page)
    out = file("/tmp/%d_cur.pdf" % doc.pk, 'w')
    tmp.write(out)
    out.close()
    pagename = "%s/doc_%04d_%04d.png" % (UPLOAD_DIR, doc.pk, num)
    mininame = "%s/doc_mini_%04d_%04d.png" % (UPLOAD_DIR, doc.pk, num)
    if convert:
        system("convert -density 400 /tmp/%d_cur.pdf -resize 25%% %s" % 
               (doc.pk, pagename))
        system("convert -density 100 /tmp/%d_cur.pdf -resize 10%% %s" % 
               (doc.pk, mininame))
    doc.add_page(num, pagename, mininame, page.bleedBox.getWidth(), 
                 page.bleedBox.getHeight())
    system("rm /tmp/%d_cur.pdf" % doc.pk)

def process_file(doc, upfile, convert=True):
    filename = UPLOAD_DIR + '/' + str(doc.pk) + '.pdf'
    # sauvegarde du document original
    fd = open(filename, 'w')
    fd.write(upfile.read())
    fd.close()

    # sauvegarde du nombre de page
    fd = file(filename, 'r')
    pdf = PdfFileReader(fd)
    doc.set_npages(pdf.numPages)

    # activate the search system
    system("pdftotext " + filename)
    words = file(UPLOAD_DIR + '/' + str(doc.pk) + '.txt', 'r') 
    doc.set_wsize(parse_words(doc, words.read()))
    words.close()

    # iteration page a page, transform en png + get page size
    num = 1
    for page in pdf.pages:
        process_page(doc, page, num, convert)
        num += 1
    fd.close()

def download_file(doc, name, url, convert=True):
    try:
        raw_doc = urlopen(url)
        process_file(doc, raw_doc, convert)
    except Exception as e:
        # NEED TO LOG!  FIXME
        print "download or process error : " + str(e)

# convert used for testing purpose
def run_process_file(doc, file, convert=True):
    if convert:
        p = Process(target=process_file, args=(doc, file))
        p.start()
    else:
        process_file(doc, file, False)

# convert used for testing purpose
def run_download_file(doc, name, url, convert=True):
    if convert:
        p = Process(target=download_file, args=(doc, name, url))
        p.start()
    else:
        download_file(doc, name, url, False)
