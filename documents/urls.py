# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from documents.models import UploadFileForm, EditForm, Document
from documents.views import upload_file, upload_http, download_file, description
from documents.views import download_page, download_mpage, edit_post, remove
from utils.decorators import AR, moderate, enforce_post
from messages.models import NewThreadForm

urlpatterns = patterns('documents.views',
    url(r'^preview/(?P<object_id>[^/]+)$',
        AR(login_required(object_detail)),
        {'queryset': Document.objects.all(),
         'template_name': 'document_prev.tpl'},
        name="document_preview"),

    url(r'^remove/(?P<id>[^/]+)$',
        moderate(login_required(remove)),
        name="document_remove"),

    url(r'^row/(?P<object_id>[^/]+)$',
        login_required(object_detail),
        {'queryset': Document.objects.all(),
         'template_name': 'document_row.tpl'},
        name="row_info"),

    url(r'^description/(?P<id>[^/]+)$',
        moderate(login_required(description)),
        name="document_desc"),

    url(r'^edit/(?P<id>[^/]+)$',
        moderate(enforce_post(login_required(edit_post))),
        name="document_edit"),

    url(r'^put/(?P<slug>[^/]+)$', 
        enforce_post(login_required(upload_file)), 
        name="upload_file"),

    url(r'^put_http/(?P<slug>[^/]+)$', 
        enforce_post(login_required(upload_http)), 
        name="upload_http_file"),

    url(r'^r/(?P<id>\d+)/.*', 
        login_required(download_file), 
        name="download_file"),

    url(r'^i/(?P<pid>[^/]+)$', 
        login_required(download_page), 
        name="download_page"),

    url(r'^m/(?P<pid>\d+)$', 
        login_required(download_mpage), 
        name="download_mpage"),

    url(r'^v/(?P<object_id>\d+)/$', 
        AR(login_required(object_detail)), 
        {'queryset': Document.objects.all(), 
         'template_name': 'viewer.tpl',
         'extra_context': {'eform': EditForm(),
                           'tform': NewThreadForm()}},
        name='view_file'),
)
