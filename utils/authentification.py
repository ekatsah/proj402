from django.http import HttpResponse
import urllib2

def intra_auth(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)
    if sid and uid:
        f = urllib2.urlopen('http://www.ulb.ac.be/commons/check?_type=normal&_sid=%s&_uid=%s' % (sid, uid))
        return HttpResponse("<pre>auth : %s %s\n\n%s</pre>" % (sid, uid, f.read(10000)))
    else:
        return HttpResponse("auth error #1")