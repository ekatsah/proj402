from django.db import models

class Course(models.Model):
    slug = models.SlugField()