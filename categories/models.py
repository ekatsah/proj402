# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.db import models
from django import forms
from courses.models import Course

class NewCategoryForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

class EditCategoryForm(forms.Form):
    id = forms.DecimalField(widget=forms.HiddenInput)
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    contains = models.ManyToManyField(Course, related_name="m2m_cat_courses")
    holds = models.ManyToManyField("self", symmetrical=False)
