# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.db import models

class WordEntry(models.Model):
    word = models.TextField();
    document = models.ForeignKey('documents.Document')
    count = models.IntegerField()

    class Meta:
        unique_together = ('word', 'document')
