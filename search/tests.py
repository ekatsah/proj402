# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.utils import unittest
from pyPdf import PdfFileReader
from django.test import Client
from search.construct import parse_words
from courses.models import Course, Category
from os import system

class SimpleTest(unittest.TestCase):
    def test_parse_words(self):
        course = Course.objects.create(slug='infoTEST', name='The testing course')
        cat = Category.objects.create(name='Project 402')
        cat.contains.add(course)

        client = Client()        
        client.login(username='admin', password='test')
        file = open('test_data/test.pdf', 'rb')
        responce = client.post('/document/put/infoTEST', 
                               {'category': 'R', 'file': file})
        file.close()
