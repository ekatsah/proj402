from settings import UPLOAD_DIR, CONVERT_PDF
from django.db import models
from os import system
from multiprocessing import Process
from pyPdf import PdfFileReader, PdfFileWriter
from search.construct import parse_words

def process_file(doc, upfile):
    filename = UPLOAD_DIR + '/' + str(doc.pk) + '.pdf'
    # sauvegarde du document original
    fd = open(filename, 'w')
    fd.write(upfile.read())
    fd.close()
    
    # sauvegarde du nombre de page
    fd = file(filename, 'r')
    pdf = PdfFileReader(fd)
    doc.set_npages(pdf.numPages)
    
    system("pdftotext " + filename)
    words = file(UPLOAD_DIR + '/' + str(doc.pk) + '.txt', 'r') 
    doc.set_wsize(parse_words(doc, words.read()))
    words.close()

    # iteration page a page, transform en png + get page size
    num = 1
    for p in pdf.pages:
        tmp = PdfFileWriter()
        tmp.addPage(p)
        out = file("/tmp/%d_cur.pdf" % doc.pk, 'w')
        tmp.write(out)
        out.close()
        pagename = "%s/doc_%03d_%04d.png" % (UPLOAD_DIR, doc.pk, num)
        if CONVERT_PDF:
            system("convert -density 400 /tmp/%d_cur.pdf -resize 25%% %s" % 
                   (doc.pk, pagename))
        doc.add_page(num, pagename, p.bleedBox.getWidth(), 
                     p.bleedBox.getHeight())
        num += 1
    fd.close()

def run_process_file(doc, file):
    p = Process(target=process_file, args=(doc, file))
    p.start()
