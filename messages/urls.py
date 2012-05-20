# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from utils.decorators import AR, enforce_post, moderate
from messages.models import Thread, Message, NewPostForm, NewThreadForm
from messages.views import post_thread, list_thread, post_msg, edit_msg
from messages.views import remove_msg
from categories.models import Category

urlpatterns = patterns('notes.views',
    url(r'^boards',
        AR(login_required(direct_to_template)),
        {'set': Category.objects.filter(name='Project 402')[0],
         'template': 'boards.tpl',
         'extra_context': {'tform': NewThreadForm()}},
        name="general_boards"),

    url(r'^list/(?P<courseid>[^/]+)/(?P<docid>[^/]+)/(?P<pageid>[^/]+)$', 
        login_required(list_thread),
        name="thread_list"),
    
    url(r'^view_thread/(?P<object_id>[^/]+)$', 
        AR(login_required(object_detail)), 
        {'queryset': Thread.objects.all(), 
         'template_name': 'thread_view.tpl',
         'extra_context': {'mform': NewPostForm()}},
        name="thread_view"),

    url(r'^post_thread$', 
        enforce_post(login_required(post_thread)), 
        name="thread_post"),
    
    url(r'^post_msg$', 
        enforce_post(login_required(post_msg)), 
        name="message_post"),
    
    url(r'^edit$',
        moderate(enforce_post(login_required(edit_msg))),
        name="message_edit"),
    
    url(r'^remove',
        moderate(enforce_post(login_required(remove_msg))),
        name="message_remove"),
)
