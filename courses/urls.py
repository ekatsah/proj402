from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_detail
from documents.models import UploadFileForm, UploadHttpForm
from courses.models import Course
from messages.models import NewThreadForm
from utils.json import json_sublist
from courses.views import new_course
from utils.decorators import AR, enforce_post, moderate

urlpatterns = patterns('courses.views',
    url(r'^new',
        moderate(enforce_post(login_required(new_course))),
        name="course_new"),

    url(r'^all$', login_required(json_sublist), 
        {'queryset': Course.objects.all,
         'fields': ['id', 'slug', 'name', 'description']},
        name='courses_all'),

    url(r'^get/(?P<slug>[^/]+)',
        login_required(object_detail),
        {'queryset': Course.objects.all(), 
         'template_name': 'course_get.tpl'},
        name="course_get"),

    url(r'^s/(?P<slug>[^/]+)', AR(login_required(object_detail)),
        {'queryset': Course.objects.all(), 
         'template_name': 'course_show.tpl',
         'extra_context': {'uform': UploadFileForm(),
                           'hform': UploadHttpForm(),
                           'tform': NewThreadForm()}},
        name='course_show'),
)
