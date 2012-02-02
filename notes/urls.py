from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from utils.decorators import AR, enforce_post
from notes.models import NewThreadForm, Thread
from notes.views import post_thread, list_thread

urlpatterns = patterns('notes.views',
    url(r'^new_thread/(?P<doc>\d+)/(?P<page>\d+)$', 
        AR(login_required(direct_to_template)), 
        {'template': 'new_thread.tpl', 
         'extra_context': {'form': NewThreadForm()}}, 
        name="new_thread"),

    url(r'^list_thread/(?P<course>[^/]+)/(?P<doc>\d+)/(?P<page>\d+)$', 
        login_required(list_thread), 
        name="list_thread"),
    
    url(r'^prev_thread/(?P<object_id>\d+)$', 
        login_required(object_detail), 
        {'queryset': Thread.objects.all(), 
         'template_name': 'preview_thread.tpl'},
        name="preview_thread"),

    url(r'^view_thread/(?P<object_id>\d+)$', 
        login_required(object_detail), 
        {'queryset': Thread.objects.all(), 
         'template_name': 'view_thread.tpl'},
        name="view_thread"),

    url(r'^post_thread$', 
        enforce_post(login_required(post_thread)), 
        name="post_thread"),
)
