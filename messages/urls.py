from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from utils.decorators import AR, enforce_post
from messages.models import Thread, Message
from messages.views import post_thread, list_thread, post_msg
from categories.models import Category

urlpatterns = patterns('notes.views',
    url(r'^boards',
        AR(login_required(direct_to_template)),
        {'set': Category.objects.filter(name='Project 402')[0],
         'template': 'boards.tpl'},
        name="general_boards"),

    url(r'^list/(?P<courseid>[^/]+)/(?P<docid>[^/]+)/(?P<pageid>[^/]+)$', 
        login_required(list_thread),
        name="thread_list"),
    
    url(r'^view_thread/(?P<object_id>\d+)$', 
        AR(login_required(object_detail)), 
        {'queryset': Thread.objects.all(), 
         'template_name': 'thread_view.tpl'},
        name="thread_view"),

    url(r'^post_thread$', 
        enforce_post(login_required(post_thread)), 
        name="thread_post"),
    
    url(r'^post_msg$', 
        enforce_post(login_required(post_msg)), 
        name="message_post"),
)
