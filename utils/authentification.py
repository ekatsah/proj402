from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from xml.dom.minidom import parseString
from string import printable
from random import choice
from settings import USER_CHECK
from urllib2 import urlopen

def get_text(nodelist):
    rc = [ node.data for node in nodelist if node.nodeType == node.TEXT_NODE ]
    return ''.join(rc)

def get_value(dom, name):
    node = dom.getElementsByTagName(name)
    if len(node) != 1:
        raise Exception("xml document not conform - please contact the admin")
    return get_text(node[0].childNodes)

def intra_auth(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)
    if sid and uid:
#        print USER_CHECK % (sid, uid)
        try:
            verifier = urlopen(USER_CHECK % (sid, uid))
        except Exception as e:
            raise Exception("ULB checker failed, error = '%s'" % str(e))
        dom = parseString(verifier.read(10000))
        ip, username = get_value(dom, "ipAddress"), get_value(dom, "username")
        firstname, name = get_value(dom, "prenom"), get_value(dom, "nom")
        email, regist = get_value(dom, "email"), get_value(dom, "matricule")
        anet = get_value(dom, "anet")
        
        if ip != request.META['REMOTE_ADDR']:
            raise Exception("ip forgery")
        
        try:
            user = User.objects.get(username=username)
        except Exception:
            rpwd = ''.join(choice(printable) for x in xrange(100))
            user = User.objects.create_user(username, email, rpwd)
            user.save()
            user.last_name = name
            user.first_name = firstname
            
            user_profile = user.profile()
            user_profile.registration = regist
            user_profile.courses = anet
            user_profile.save()
            user.save()

        user.backend = 'django.contrib.auth.backends.ModelBackend' 
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    else:
        raise Exception("auth param not found")
