from django.conf.urls.defaults import patterns, url
from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from upload.models import Document

urlpatterns = patterns('users.views',
    url(r'^v/(?P<object_id>\d+)/$', login_required(object_detail), 
        {'queryset': Document.objects.all(), 'template_name': 'viewer.tpl'},
        name='view_file'),
)
