from django.db import models

class Course(models.Model):
    slug = models.CharField(max_length=40)