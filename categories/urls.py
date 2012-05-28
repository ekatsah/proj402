# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from categories.views import sub_categories, attach_category, detach_category
from categories.views import del_category, new_category, attach_course
from categories.views import detach_course, sub_courses, edit_category
from categories.models import Category
from utils.decorators import enforce_post, chk_perm
from utils.json import json_sublist_send

urlpatterns = patterns('categories.views',
    url(r'^new',
        enforce_post(chk_perm(login_required(new_category), 'structure_manage')),
        name="category_new"),

    url(r'^edit$',
        enforce_post(chk_perm(login_required(edit_category), 'structure_manage')),
        name="category_edit"),

    url(r'^attach/(?P<category>[^/]+)/(?P<subcategory>[^/]+)$', 
        chk_perm(login_required(attach_category), 'structure_manage'),
        name="category_attach"),

    url(r'^detach/(?P<category>[^/]+)/(?P<parent>[^/]+)$',
        chk_perm(login_required(detach_category), 'structure_manage'),
        name="category_detach"),

    url(r'^add_course/(?P<category>[^/]+)/(?P<slug>[^/]+)$',
        chk_perm(login_required(attach_course), 'structure_manage'),
        name="cat_course_add"),

    url(r'^del_course/(?P<category>[^/]+)/(?P<slug>[^/]+)$',
        chk_perm(login_required(detach_course), 'structure_manage'),
        name="cat_course_del"),

    url(r'^del/(?P<category>[^/]+)$',
        chk_perm(login_required(del_category), 'structure_manage'),
        name='category_del'),

    url(r'^sub/(?P<catid>[^/]+)$', 
        login_required(sub_categories), name='category_sub'),

    url(r'^sub_courses/(?P<catid>[^/]+)$', 
        login_required(sub_courses), name='courses_by_cat'),

    url(r'^all$', login_required(json_sublist_send), 
        {'queryset': Category.objects.order_by("id"), 
         'fields': ['id', 'name', 'description', 'contains', 'holds']},
        name='categories_all'),
)
