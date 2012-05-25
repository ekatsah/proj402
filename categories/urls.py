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
from utils.decorators import enforce_post, moderate
from utils.json import json_sublist_send

urlpatterns = patterns('categories.views',
    url(r'^new',
        moderate(enforce_post(login_required(new_category))),
        name="category_new"),

    url(r'^edit$',
        enforce_post(moderate(login_required(edit_category))),
        name="category_edit"),

    url(r'^attach/(?P<category>[^/]+)/(?P<subcategory>[^/]+)$', 
        moderate(login_required(attach_category)),
        name="category_attach"),

    url(r'^detach/(?P<category>[^/]+)/(?P<parent>[^/]+)$',
        moderate(login_required(detach_category)),
        name="category_detach"),

    url(r'^add_course/(?P<category>[^/]+)/(?P<slug>[^/]+)$',
        moderate(login_required(attach_course)),
        name="cat_course_add"),

    url(r'^del_course/(?P<category>[^/]+)/(?P<slug>[^/]+)$',
        moderate(login_required(detach_course)),
        name="cat_course_del"),

    url(r'^del/(?P<category>[^/]+)$',
        moderate(login_required(del_category)),
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
