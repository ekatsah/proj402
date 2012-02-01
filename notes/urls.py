from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from utils.decorators import AR, enforce_post
from notes.models import NewThreadForm
from notes.views import post_thread

urlpatterns = patterns('notes.views',
    url(r'^new_thread/(?P<doc>\d+)/(?P<page>\d+)$', 
        AR(login_required(direct_to_template)), 
        {'template': 'new_thread.tpl', 
         'extra_context': {'form': NewThreadForm()}}, 
        name="new_thread"),
                       
    url(r'^post_thread$', 
        enforce_post(login_required(post_thread)), 
        name="post_thread"),
)
