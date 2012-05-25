# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from utils.decorators import AR, moderate, enforce_post
from users.views import mask_welcome, get_courses, follow, unset_modo, set_modo
from users.views import new_user, unfollow

urlpatterns = patterns('users.views',
    url(r'^$',
        AR(login_required(direct_to_template)),
        {'template': 'user_show.tpl'},
        name='profile'),

    url(r'^mask_welcome$',
        AR(login_required(mask_welcome)),
        name='mask_welcome'),

    url(r'^courses$',
        login_required(get_courses),
        name="user_courses"),

    url(r'^follow$',
        require_POST(login_required(follow)),
        name="user_follow"),

    url(r'^unfollow$',
        require_POST(login_required(unfollow)),
        name="user_unfollow"),

    url(r'^login/$', login, {'template_name': 'user_login.tpl'}, name="user_login"),
    url(r'^logout/$', logout, {'next_page': '/'}, name="user_logout"),

    url(r'^set_modo/(?P<uid>[^/]+)$',
        moderate(login_required(set_modo)),
        name="user_set_modo"),

    url(r'^unset_modo/(?P<uid>[^/]+)$',
        moderate(login_required(unset_modo)),
        name="user_unset_modo"),

    url(r'^new$',
        enforce_post(moderate(login_required(new_user))),
        name='user_new'),
)
