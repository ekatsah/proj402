# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from upvotes.views import vote_doc

urlpatterns = patterns('upvotes.views', 
    url(r'^doc/(?P<id>\d+)/(?P<category>[ROSEPLDT])/(?P<score>[-1]+)$', 
        login_required(vote_doc), 
        name='vote_doc'),
)
