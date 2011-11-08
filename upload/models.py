from django.db import models
from django import forms

# Create your models here.

class UploadFileForm(forms.Form):
    file  = forms.FileField()