from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_detail
from courses.models import Course
from utils.json import json_list

urlpatterns = patterns('courses.views',
    url(r'^all$', login_required(json_list), {'queryset': Course.objects.all()},
        name='course_all'),
    url(r'^s/(?P<slug>[^/]+)', login_required(object_detail), {'queryset': Course.objects.all(), 
                                                              'template_name': 'course_show.tpl'},
        name='course_show'),
)
