from django.db import models
from upload.models import Document

class Course(models.Model):
    slug = models.SlugField()
    name = models.TextField()
    documents = models.ManyToManyField(Document)

    def add_document(self, document):
        self.documents.add(document)
