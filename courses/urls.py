from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_detail
from courses.models import Course, Category
from utils.json import json_sublist
from courses.views import subcategory, courses_by_cat
from utils.decorators import AR

urlpatterns = patterns('courses.views',
    url(r'^all$', login_required(json_sublist), 
        {'queryset': Course.objects.all(),
         'fields': ['id', 'slug', 'name', 'description']},
        name='courses_all'),

    url(r'^sub/(?P<catid>[^/]+)$', login_required(courses_by_cat), 
        name='courses_by_cat'),

    url(r'^categories/all$', login_required(json_sublist), 
        {'queryset': Category.objects.all(), 
         'fields': ['id', 'name', 'description', 'contains', 'holds']},
        name='category_all'),

    url(r'^categories/sub/(?P<catid>[^/]+)$', login_required(subcategory), 
        name='category_sub'),

    url(r'^get/(?P<slug>[^/]+)',
        login_required(object_detail),
        {'queryset': Course.objects.all(), 
         'template_name': 'course_get.tpl'},
        name="course_get"),

    url(r'^s/(?P<slug>[^/]+)', AR(login_required(object_detail)),
        {'queryset': Course.objects.all(), 
         'template_name': 'course_show.tpl'},
        name='course_show'),
)
