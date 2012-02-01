from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from notes.models import NewThreadForm, Thread, Note
from django.core.urlresolvers import reverse
from courses.models import Course
from upload.models import Page, Document

def post_thread(request):
    form = NewThreadForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data;
        thread = Thread.objects.create(subject=data['subject'])
        note = Note.objects.create(owner=request.user, thread=thread, 
                                   text=data['message'])
        thread.notes.add(note)
        try:
            thread.referd = Document.objects.get(pk=data['document'])
        except Exception:
            pass
        try:
            thread.referp = Page.objects.get(pk=data['page'])
        except Exception:
            pass
        try:
            thread.referc = Course.objects.get(pk=data['course'])
        except Exception:
            pass
        thread.save()
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")
