# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from documents.models import EditForm, Document
from documents.views import upload_file, upload_http, download_file, description
from documents.views import download_page, download_mpage, edit_post, remove 
from documents.views import doc_by_course, doc_pending
from utils.decorators import AR, chk_perm, enforce_post
from utils.json import json_sublist_send
from messages.models import NewThreadForm

urlpatterns = patterns('documents.views',
    url(r'^remove/(?P<object_id>[^/]+)$',
        chk_perm(login_required(remove), 'document_manage'),
        name="document_remove"),

    url(r'^all$',
        login_required(json_sublist_send),
        {'queryset': Document.objects.all,
         'fields': ['id', 'name', 'description', 'size', 'done', 'refer.name', 
                    'refer.id', 'date', 'points.score', 'owner.get_profile.real_name', 
                         'points.full_category', 'points.category']},
        name="document_all"),

    url(r'^all/(?P<slug>[^/]+)$',
        login_required(doc_by_course),
        name="document_by_course"),

    url(r'^pending/(?P<slug>[^/]+)$',
        login_required(doc_pending),
        name="document_pending"),

    url(r'^description/(?P<id>[^/]+)$',
        login_required(description),
        name="document_desc"),

    url(r'^edit/(?P<object_id>[^/]+)$',
        chk_perm(enforce_post(login_required(edit_post)), 'document_edit'),
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

    url(r'^v/(?P<object_id>[^/]+)/$', 
        AR(login_required(object_detail)), 
        {'queryset': Document.objects.all(), 
         'template_name': 'viewer.tpl',
         'extra_context': {'eform': EditForm(),
                           'tform': NewThreadForm()}},
        name='view_file'),
)
