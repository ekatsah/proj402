from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from messages.models import NewThreadForm, Thread, Message
from documents.models import Page, Document
from courses.models import Course

def post_thread(request):
    form = NewThreadForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data;
        thread = Thread.objects.create(subject=data['subject'], 
                                       poster=request.user)
        msg = Message.objects.create(owner=request.user, thread=thread, 
                                     text=data['message'])
        thread.msgs.add(msg)

        # FIXME check coherence between course, doc, page before create
        course = get_object_or_404(Course, pk=data['course'])
        doc, page = None, None
        course.threads.add(thread)
        try:
            doc = Document.objects.get(pk=data['document'])
            doc.threads.add(thread)
            page = Page.objects.get(pk=data['page'])
            page.threads(thread)
        except Exception:
            pass
        
        thread.referp = page
        thread.referd = doc
        thread.referc = course
        thread.save()
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")

def new_thread(request, courseid, docid, pageid):
    course = get_object_or_404(Course, pk=courseid)
    doc, page = None, None

    if docid != "0":
        doc = get_object_or_404(Document, pk=docid)
        if doc not in course.documents:
            raise Exception("Corrupt Query, step doc")

    if pageid != "0":
        page = get_object_or_404(Page, pk=pageid)
        if page not in doc.pages:
            raise Exception("Corrupt Query, step page")

    return render_to_response('new_thread.tpl',
                {'course': course, 'form': NewThreadForm(), 
                 'document': doc, 'page': page}, 
                context_instance=RequestContext(request))

def list_thread(request, courseid, docid, pageid):
    course = get_object_or_404(Course, pk=courseid)
    set = course.threads.all()
    doc, page = None, None

    if docid != "0":
        doc = get_object_or_404(Document, pk=docid)
        if doc not in course.documents:
            raise Exception("Corrupt Query, step doc")
        set = doc.threads.all()

    if pageid != "0":
        page = get_object_or_404(Page, pk=pageid)
        if page not in doc.pages:
            raise Exception("Corrupt Query, step page")
        set = page.threads.all()

    return render_to_response('list_thread.tpl',
                {'threads': set, 'page': page, 'course': course, 'document': doc},
                context_instance=RequestContext(request))
