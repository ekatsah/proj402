# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.html import escape
from documents.models import UploadFileForm, UploadHttpForm, EditForm
from documents.models import Document, Page, PendingDocument
from users.models import Permission
from courses.models import Course
from utils.json import json_sublist_send, json_object_send
from urllib import unquote
from re import match

def upload_file(request, slug):
    form = UploadFileForm(request.POST, request.FILES)

    if form.is_valid() and match(r'.*\.[pP][dD][fF]$',
                                 request.FILES['file'].name):
        course = get_object_or_404(Course, slug=slug)
        doc = Document.new(request.user, course, escape(request.FILES['file'].name),
                           escape(form.cleaned_data['category']))
        course.add_document(doc)

        url = '/tmp/TMP402_%d.pdf' % doc.id
        tmp_doc = open(url, 'w')
        tmp_doc.write(request.FILES['file'].read())
        tmp_doc.close()
        Permission.objects.create(name='document_edit', user=request.user,
                                  object_id=doc.id)
        PendingDocument.objects.create(doc=doc, state="queued", url='file://' + url)
        return HttpResponseRedirect(reverse('course_show', args=[slug]))
    return HttpResponse('form invalid', 'text/html')

def upload_http(request, slug):
    form = UploadHttpForm(request.POST)
    if form.is_valid():
        course = get_object_or_404(Course, slug=slug)
        url = escape(form.cleaned_data['url'])
        name = match(r'.*/([^/]+)$', url).group(1)
        if "%" in name:
            name = unquote(name)
        if len(name) < 4:
            return HttpResponse('name invalid', 'text/html')
        doc = Document.new(request.user, course, name.replace("_", " "),
                           escape(form.cleaned_data['category']))
        course.add_document(doc)
        request.user.add_row_perm(doc, '')
        Permission.objects.create(name='document_edit', user=request.user,
                                  object_id=doc.id)
        PendingDocument.objects.create(doc=doc, state="queued", url=url)
        return HttpResponse('ok', 'text/html')
    return HttpResponse('form invalid', 'text/html')

def download_file(request, id):
    document = get_object_or_404(Document, pk=id)
    response = HttpResponse(document.get_content(), mimetype="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=' + document.pretty_name()
    response['Content-Length'] = document.weight()
    return response

def download_page(request, pid=None):
    page = get_object_or_404(Page, pk=pid)
    return HttpResponse(page.get_content(), mimetype="image/jpeg")

def download_mpage(request, pid=None):
    page = get_object_or_404(Page, pk=pid)
    return HttpResponse(page.get_mini(), mimetype="image/jpeg")

def edit_post(request, object_id):
    doc = get_object_or_404(Document, pk=object_id)
    form = EditForm(request.POST)
    if form.is_valid():
        doc.name = escape(form.cleaned_data['name'])
        doc.description = escape(form.cleaned_data['description'])
        doc.save()
        return HttpResponse('ok', 'text/html')
    else:
        return HttpResponse('form invalid', 'text/html')

def remove(request, object_id):
    doc = get_object_or_404(Document, pk=object_id)
    doc.delete()
    return HttpResponse('ok', 'text/html')

def description(request, id):
    doc = get_object_or_404(Document, pk=id)
    return json_object_send(request, doc, ['id', 'name', 'description'])

def doc_by_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return json_sublist_send(request, course.documents.all,
                        ['id', 'name', 'description', 'size', 'done', 'points.category',
                         'refer.name', 'refer.id', 'date', 'points.score',
                         'owner.get_profile.real_name', 'points.full_category'])

def doc_pending(request, slug):
    course = get_object_or_404(Course, slug=slug)
    qs = PendingDocument.objects.filter(doc__refer=course).exclude(state__exact="done")
    return json_sublist_send(request, [task.doc for task in qs], ['id', 'done', 'size'])
