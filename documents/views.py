# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.db import transaction
from documents.models import UploadFileForm, UploadHttpForm
from documents.models import EditForm, Document, Page
from courses.models import Course
from re import match

@transaction.commit_manually
def upload_file(request, slug):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        course = get_object_or_404(Course, slug=slug)
        d = Document.new(request.user, course, request.FILES['file'].name, 
                         form.cleaned_data['category'])
        course.add_document(d)
        transaction.commit()
        #run_process_file(d.id, request.FILES['file'])
    # FIXME add an error management
    return HttpResponseRedirect(reverse('course_show', args=[slug]))

# FIXME MAJOR REFACTOR NEEDED (/me begins to crash)
@transaction.commit_manually
def upload_http(request, slug):
    form = UploadHttpForm(request.POST)
    if form.is_valid():
        course = get_object_or_404(Course, slug=slug)
        url = form.cleaned_data['url']
        name = match(r'.*/([^/]+)$', url).group(1)
        if len(name) < 4:
            return HttpResponse('name invalid', 'text/html')
        d = Document.new(request.user, course, name, 
                         form.cleaned_data['category'])
        course.add_document(d)
        transaction.commit()
        #run_download_file(d.id, url)
        return HttpResponse('ok', 'text/html')
    return HttpResponse('form invalid', 'text/html')

def download_file(request, id):
    document = get_object_or_404(Document, pk=id)
    response = HttpResponse(document.get_content(), mimetype="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=' + document.pretty_name()
    return response

def download_page(request, pid=None):
    page = get_object_or_404(Page, pk=pid)
    return HttpResponse(page.get_content(), mimetype="image/jpeg")

def download_mpage(request, pid=None):
    page = get_object_or_404(Page, pk=pid)
    return HttpResponse(page.get_mini(), mimetype="image/jpeg")

def edit_post(request, id):
    doc = get_object_or_404(Document, pk=id)
    form = EditForm(request.POST)
    if form.is_valid():
        doc.name = form.cleaned_data['name']
        doc.description = form.cleaned_data['description']
        doc.save()
        return HttpResponse('ok', 'text/html')
    else:
        return HttpResponse('form invalid', 'text/html')
    
def remove(request, id):
    doc = get_object_or_404(Document, pk=id)
    doc.delete()
    return HttpResponse('ok', 'text/html')

def description(request, id):
    doc = get_object_or_404(Document, pk=id)
    return HttpResponse('{"id": %d, "name":"%s", "description":"%s"}' %
                        (doc.id, doc.name, doc.description),
                        'application/json')
