from django.db import models
from django import forms
from django.contrib.auth.models import User

class NewThreadForm(forms.Form):
    file  = forms.FileField()

class Thread(models.Model):
    subject = models.TextField();
    notes = models.ManyToManyField("Note", related_name="back_thread")
    referp = models.ForeignKey('upload.Page', related_name="back_tpage", null=True)
    referd = models.ForeignKey('upload.Document', related_name="back_tdoc", null=True)
    referc = models.ForeignKey('courses.Course', related_name="back_tcourse", null=True)

class Note(models.Model):
    owner = models.ForeignKey(User)
    thread = models.ManyToManyField(Thread)
    text = models.TextField();
