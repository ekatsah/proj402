from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from admin.views import catadd, catnew, catrm
from utils.json import json_list
from utils.decorators import AR

urlpatterns = patterns('admin.views',
    url(r'^tree$', AR(login_required(direct_to_template)), 
        {'template': 'adm_tree.tpl'}, name="category_tree"),

    url(r'^tree/catadd/(?P<category>[^/]+)/(?P<subcategory>[^/]+)$', 
        login_required(catadd), name="adm_tree_add"),

    url(r'^tree/catnew/(?P<category>[^/]+)/(?P<name>[^/]+)$', 
        login_required(catnew), name="adm_tree_new"),

    url(r'^tree/catrm/(?P<category>[^/]+)/(?P<parent>[^/]+)$',
        login_required(catrm), name="adm_tree_rm"),

    url(r'', AR(login_required(direct_to_template)), 
        {'template': 'admin.tpl'}, name="admin_index"),
)
