from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime

class NewThreadForm(forms.Form):
    subject = forms.CharField();
    message = forms.CharField(widget=forms.Textarea)
    course = forms.DecimalField(widget=forms.HiddenInput)
    document = forms.DecimalField(widget=forms.HiddenInput)
    page = forms.DecimalField(widget=forms.HiddenInput)

class NewPostForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    thread = forms.DecimalField(widget=forms.HiddenInput)
    reference = forms.DecimalField(widget=forms.HiddenInput)

class Thread(models.Model):
    subject = models.TextField();
    msgs = models.ManyToManyField("Message", related_name="back_thread")
    poster = models.ForeignKey(User)
    referp = models.ForeignKey('documents.Page', related_name="back_tpage", null=True)
    referd = models.ForeignKey('documents.Document', related_name="back_tdoc", null=True)
    referc = models.ForeignKey('courses.Course', related_name="back_tcourse", null=True)

class Message(models.Model):
    owner = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    reference = models.ForeignKey("self", null=True)
