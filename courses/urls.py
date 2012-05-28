# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_detail, object_list
from documents.models import UploadFileForm, UploadHttpForm
from courses.models import Course
from messages.models import NewThreadForm
from upvotes.models import CAT_DOCUMENTS
from utils.json import json_sublist_send, json_select_send
from courses.views import new_course
from utils.decorators import AR, enforce_post, chk_perm

urlpatterns = patterns('courses.views',
    url(r'^new',
        enforce_post(chk_perm(login_required(new_course), 'structure_manage')),
        name="course_new"),

    url(r'^all$', login_required(json_sublist_send), 
        {'queryset': Course.objects.all,
         'fields': ['id', 'slug', 'name', 'description']},
        name='courses_all'),

    url(r'get/(?P<slug>[^/]+)',
        login_required(json_select_send),
        {'queryset': Course.objects.all,
         'fields': ['id', 'slug', 'name', 'description']},
        name='course_get'),

    url(r'^s/(?P<slug>[^/]+)', AR(login_required(object_detail)),
        {'queryset': Course.objects.all(), 
         'template_name': 'course_show.tpl',
         'extra_context': {'uform': UploadFileForm(),
                           'hform': UploadHttpForm(),
                           'tform': NewThreadForm(),
                           'doc_categories': CAT_DOCUMENTS}},
        name='course_show'),

    url(r'^view_all', AR(login_required(object_list)),
        {'queryset': Course.objects.exclude(slug__startswith="402"), 
         'template_name': 'course_all.tpl'},
        name='course_view_all'),
)
