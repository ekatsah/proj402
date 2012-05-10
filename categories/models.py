from django.db import models
from django import forms
from courses.models import Course

class NewCategoryForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    contains = models.ManyToManyField(Course, related_name="m2m_cat_courses")
    holds = models.ManyToManyField("self", symmetrical=False)
