# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.html import escape
from django.core.urlresolvers import reverse
from messages.models import NewThreadForm, NewPostForm, Thread, Message
from documents.models import Page, Document
from courses.models import Course
from utils.json import json_string

def post_thread(request):
    form = NewThreadForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        thread = Thread.objects.create(subject=escape(data['subject']), 
                                       poster=request.user)
        msg = Message.objects.create(owner=request.user, thread=thread, 
                                     text=escape(data['message']))
        thread.msgs.add(msg)

        # FIXME check coherence between course, doc, page before create
        course = get_object_or_404(Course, pk=data['course'])
        doc, page = None, None
        course.threads.add(thread)
        try:
            doc = Document.objects.get(pk=data['document'])
            doc.threads.add(thread)
            page = Page.objects.get(pk=data['page'])
            page.threads.add(thread)
        except Exception:
            pass
        
        thread.referp = page
        thread.referd = doc
        thread.referc = course
        thread.save()
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")

def list_thread(request, courseid, docid, pageid):
    course = get_object_or_404(Course, pk=courseid)
    set = course.threads.all()
    doc, page = None, None

    if docid != "0":
        doc = get_object_or_404(Document, pk=docid)
        if doc not in course.documents.all():
            raise Exception("Corrupt Query, step doc")
        set = doc.threads.all()

    if pageid != "0":
        page = get_object_or_404(Page, pk=pageid)
        if page not in doc.pages.all():
            raise Exception("Corrupt Query, step page")
        set = page.threads.all()

    threads = list()
    for thread in set:
        count = len(thread.msgs.all())
        orig, last = thread.msgs.all()[0], thread.msgs.all()[count - 1]
        threads.append("""{"id": %d, "subject": "%s", "length": %d, "date_min":
            "%s", "owner_id": %d, "date_max": "%s", "owner_name": "%s %s"}""" % 
            (thread.id, json_string(thread.subject), count,
             orig.date.strftime("%d/%m/%y %H:%M"), thread.poster.id, 
             last.date.strftime("%d/%m/%y %H:%M"), thread.poster.first_name, 
             thread.poster.last_name))
    return HttpResponse('[%s]' % ','.join(threads), 'application/javascript')

def post_msg(request):
    form = NewPostForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        thread = get_object_or_404(Thread, pk=data['thread'])
        reference = get_object_or_404(Message, pk=data['reference'])
        msg = Message.objects.create(owner=request.user, thread=thread, 
                                     text=escape(data['message']),
                                     reference=reference)
        thread.msgs.add(msg)
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")

def edit_msg(request):
    form = NewPostForm(request.POST)
    if form.is_valid():
        pass

def remove_msg(request):
    pass