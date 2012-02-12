from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from utils.decorators import AR, enforce_post
from messages.models import Thread
from messages.views import post_thread, list_thread, new_thread
from courses.models import Category

urlpatterns = patterns('notes.views',
    url(r'^boards',
        AR(login_required(direct_to_template)),
        {'set': Category.objects.filter(name='Project 402')[0],
         'template': 'boards.tpl'},
        name="general_boards"),

    url(r'^new_thread/(?P<courseid>[^/]+)/(?P<docid>[^/]+)/(?P<pageid>[^/]+)$', 
        login_required(new_thread), 
        name="new_thread"),

    url(r'^list_thread/(?P<courseid>[^/]+)/(?P<docid>[^/]+)/(?P<pageid>[^/]+)$', 
        login_required(list_thread),
        name="list_thread"),
    
    url(r'^prev_thread/(?P<object_id>\d+)$', 
        login_required(object_detail), 
        {'queryset': Thread.objects.all(), 
         'template_name': 'preview_thread.tpl'},
        name="preview_thread"),

    url(r'^view_thread/(?P<object_id>\d+)$', 
        AR(login_required(object_detail)), 
        {'queryset': Thread.objects.all(), 
         'template_name': 'view_thread.tpl'},
        name="view_thread"),

    url(r'^post_thread$', 
        enforce_post(login_required(post_thread)), 
        name="post_thread"),
)
