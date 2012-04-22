from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def mask_welcome(request):
    up = request.user.profile
    up.welcome = False
    up.save()
    return HttpResponseRedirect(reverse('profile'))
