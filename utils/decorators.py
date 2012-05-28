# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden

# Ajax rewrite.
def AR(function):
    def check_ajax(request, *args, **kwargs):
        if (request.is_ajax()):
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/zoidberg#' + request.path)
    return check_ajax

# enforce a post request
def enforce_post(function):
    def check_post(request, *args, **kwargs):
        if request.method == 'POST':
            return function(request, *args, **kwargs)
        else:
            return HttpResponse("Error: Not a POST request")
    return check_post

# enforce acl rights
def chk_perm(function, perm):
    def check(request, *args, **kwargs):
        # check if user has global permission
        if request.user.get_profile().has_perm(perm):
            return function(request, *args, **kwargs)
        else:
            # try to find a object_id
            id = 0
            if 'object_id' in kwargs:
                id = kwargs['object_id']
            elif 'object_id' in request.REQUEST:
                id = request.REQUEST['object_id']

            # check if user has row permission
            if id and request.user.get_profile().has_perm(perm, id):
                return function(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You don't have permissions to " + 
                                             "access this part of the website.")
    return check
