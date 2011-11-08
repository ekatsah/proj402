from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class UploadFileForm(forms.Form):
    file  = forms.FileField()

class Document(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User)
    refer = models.ForeignKey('courses.Course', related_name="back_course")

    @classmethod
    def new(cls, owner, course, file):
        doc = cls(name=file.name, owner=owner, refer=course)
        doc.save()
        f = open('upload/r/' + str(doc.pk) + '.pdf', 'w+')
        f.write(file.read())
        f.close()
        return doc
    
    def get_content(self):
        f = open('upload/r/' + str(self.pk) + '.pdf', 'r')
        content = f.read()
        f.close()
        return content
