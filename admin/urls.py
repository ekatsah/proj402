from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from utils.decorators import AR
from courses.models import NewCourseForm
from categories.models import NewCategoryForm
from documents.models import Document

urlpatterns = patterns('admin.views',
    url(r'^tree$', AR(login_required(direct_to_template)), 
        {'template': 'adm_tree.tpl',
         'extra_context': {'nform': NewCourseForm(),
                           'cform': NewCategoryForm()}}, 
        name="category_tree"),

    url(r'^users$', AR(login_required(object_list)), 
        {'template_name': 'adm_users.tpl',
         'queryset': User.objects.all()}, 
        name="admin_users"),

    url(r'^documents$', AR(login_required(object_list)), 
        {'template_name': 'adm_documents.tpl',
         'queryset': Document.objects.all()}, 
        name="admin_documents"),

    url(r'', AR(login_required(direct_to_template)), 
        {'template': 'admin.tpl'}, name="admin_index"),
)
