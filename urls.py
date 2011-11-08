from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^$', direct_to_template, {'template': 'base.tpl'}, name='index'),
    url(r'^user/', include('users.urls'), name='users'),
    url(r'^course/', include('courses.urls'), name='courses'),
    url(r'^upload/', include('upload.urls'), name='upload'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
