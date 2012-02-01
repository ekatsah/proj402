from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from notes.models import NewThreadForm, Thread, Note
from courses.models import Course
from upload.models import Page, Document

def post_thread(request):
    form = NewThreadForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data;
        thread = Thread.objects.create(subject=data['subject'], 
                                       poster=request.user)
        note = Note.objects.create(owner=request.user, thread=thread, 
                                   text=data['message'])
        thread.notes.add(note)
        try:
            thread.referd = Document.objects.get(pk=data['document'])
        except Exception:
            pass
        try:
            page = Page.objects.get(pk=data['page'])
            thread.referp = page
            page.threads.add(thread)
        except Exception:
            pass
        try:
            thread.referc = Course.objects.get(pk=data['course'])
        except Exception:
            pass
        thread.save()
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")

def list_thread(request, course, doc, page):
    if course == "null":
        # thread about a document page
        page = get_object_or_404(Page, pk=page)
        qs = page.threads.all()
    return render_to_response('list_thread.tpl',
                {'threads': qs}, context_instance=RequestContext(request))