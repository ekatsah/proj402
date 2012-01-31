from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from utils.decorators import AR

urlpatterns = patterns('notes.views',
    url(r'^new_thread/(?P<doc>\d+)/(?P<page>\d+)$', AR(login_required(direct_to_template)), 
        {'template': 'new_thread.tpl'}, name='new_thread'),
)
