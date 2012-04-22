from django.db import models, connection
from django import forms
from django.contrib.auth.models import User
from settings import UPLOAD_DIR
from utils.splitter import run_process_file
from upvotes.models import VoteDocument, CAT_DOCUMENTS
 
# Create your models here.

class UploadFileForm(forms.Form):
    category = forms.ChoiceField(choices=CAT_DOCUMENTS)
    file  = forms.FileField()

class EditForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)

class Page(models.Model):
    num = models.IntegerField()
    filename = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    threads = models.ManyToManyField('messages.Thread')
    
    def get_content(self):
        f = open(self.filename, 'r')
        content = f.read()
        f.close()
        return content

class Document(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User)
    refer = models.ForeignKey('courses.Course', related_name="back_course")
    size = models.IntegerField(null=True)
    words = models.IntegerField(null=True, default=0)
    ready = models.BooleanField(default=False)
    pages = models.ManyToManyField(Page)
    threads = models.ManyToManyField('messages.Thread')
    done = models.IntegerField(null=False)
    points = models.ForeignKey(VoteDocument)
    date = models.DateTimeField(auto_now=True, null=False)
    description = models.TextField()
    
    @classmethod
    def new(cls, owner, course, file, category, convert=True):
        vd = VoteDocument.objects.create(category=category)
        doc = cls(name=file.name, owner=owner, refer=course, done=0, size=1,
                  points=vd)
        doc.save()
        run_process_file(doc, file, convert)
        return doc
    
    def get_content(self):
        f = open(UPLOAD_DIR + '/' + str(self.pk) + '.pdf', 'r')
        content = f.read()
        f.close()
        return content

    def set_npages(self, num):
        self.size = num
        self.save()

    def set_wsize(self, num):
        self.words = num
        self.save()

    def add_page(self, num, fname, w, h):
        p = Page(num=num, filename=fname, width=w, height=h)
        p.save()
        self.pages.add(p)

        cursor = connection.cursor()
        cursor.execute('UPDATE documents_document SET done = done + 1 WHERE id = %d' % self.id)
        connection.commit_unless_managed()
        cursor.close()

    def edit_form(self):
        return EditForm(initial={'name': self.name, 
                                 'description': self.description})

    def pretty_name(self):
        name = self.name.lower().replace(' ', '_')
        if not name.endswith('.pdf'):
            name += '.pdf'
        return name