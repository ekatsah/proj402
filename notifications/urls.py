# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
from notifications.models import Event
from utils.decorators import AR

urlpatterns = patterns('notifications.views',
    url(r'^wall',
        AR(login_required(object_list)),
        {'queryset': Event.objects.order_by("-date")[:20],
         'template_name': 'wall.tpl'},
        name="wall"),
)
