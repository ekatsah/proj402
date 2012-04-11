from django.utils import unittest
from pyPdf import PdfFileReader
from search.construct import parse_words
from os import system

class SimpleTest(unittest.TestCase):
    def test_parse_words(self):
        system("pdftotext test_data/test.pdf")
        words = file('test_data/test.txt', 'r')
        parse_words(None, words.read())
        words.close()
