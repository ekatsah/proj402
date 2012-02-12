from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from utils.decorators import AR

urlpatterns = patterns('',
    url(r'^user/', include('users.urls'), name='users'),
    url(r'^course/', include('courses.urls'), name='courses'),
    url(r'^document/', include('documents.urls'), name='documents'),
    url(r'^msg/', include('messages.urls'), name='messages'),
    url(r'^admin/', include('admin.urls'), name='admin'),
    
    url(r'^$', direct_to_template, {'template': 'layout.tpl'}, name='index'),

    # entry point
    url(r'^zoidberg$', login_required(direct_to_template), 
        {'template': 'base.tpl'}, name='index'),

    url('^help$', AR(direct_to_template), {'template': 'help.tpl'}, name='help'),
)
