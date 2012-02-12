from django.db import models
from documents.models import Document

class Course(models.Model):
    slug = models.SlugField()
    name = models.TextField()
    description = models.TextField(null=True)
    documents = models.ManyToManyField(Document)
    threads = models.ManyToManyField("messages.Thread")

    def add_document(self, document):
        self.documents.add(document)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    contains = models.ManyToManyField(Course)
    holds = models.ManyToManyField("self", symmetrical=False)