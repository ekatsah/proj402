from django.db import models

class WordEntry(models.Model):
    word = models.TextField();
    document = models.ForeignKey('documents.Document')
    count = models.IntegerField()

    class Meta:
        unique_together = ('word', 'document')
