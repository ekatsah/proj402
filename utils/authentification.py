# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import login
from django.utils.html import escape
from xml.dom.minidom import parseString
from string import printable
from random import choice
from settings import USER_CHECK
from urllib2 import urlopen
from base64 import b64encode

def get_text(nodelist):
    rc = [ node.data for node in nodelist if node.nodeType == node.TEXT_NODE ]
    return ''.join(rc)

def get_value(dom, name):
    node = dom.getElementsByTagName(name)
    if len(node) != 1:
        raise Exception("xml document not conform - please contact the admin")
    return escape(get_text(node[0].childNodes))

def intra_auth(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)
    if sid and uid:
        try:
            verifier = urlopen(USER_CHECK % (sid, uid))
            infos = verifier.read()
        except Exception as e:
            return render_to_response('error.tpl', 
                                      {'msg': "ULB ERR#1: " + str(e)},
                                      context_instance=RequestContext(request))

        dom = parseString(infos)
        try:
            ip, username = get_value(dom, "ipAddress"), get_value(dom, "username")
            first_name = get_value(dom, "prenom").capitalize()
            last_name = get_value(dom, "nom").capitalize()
            email, regist = get_value(dom, "email"), get_value(dom, "matricule")
            anet, facid = get_value(dom, "anet"), get_value(dom, "facid")
        except:
            msg = b64encode(infos)
            msg = [ msg[y * 78:(y+1)*78] for y in xrange((len(msg)/78) +1) ]
            return render_to_response('error.tpl', {'msg': "\n".join(msg)},
                                      context_instance=RequestContext(request))
        try:
            user = User.objects.get(username=username)
        except Exception:
            rpwd = ''.join(choice(printable) for x in xrange(100))
            user = User.objects.create_user(username, email, rpwd)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

        user_profile = user.profile
        user_profile.registration = regist
        user_profile.section = facid + ':' + anet
        user_profile.save()
        user.save()

        user.backend = 'django.contrib.auth.backends.ModelBackend' 
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    else:
        raise Exception("auth param not found")
