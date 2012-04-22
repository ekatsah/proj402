from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from documents.models import UploadFileForm, EditForm, Document
from documents.views import upload_file, download_file, download_page, edit_post
from utils.decorators import AR

urlpatterns = patterns('documents.views',
    url(r'^get$', 
        AR(login_required(direct_to_template)), 
        {'template': 'upload_form.tpl', 
         'extra_context': {'form': UploadFileForm()}}, 
        name="upload_form"),

    url(r'^preview/(?P<object_id>[^/]+)$',
        AR(login_required(object_detail)),
        {'queryset': Document.objects.all(),
         'template_name': 'document_prev.tpl'},
        name="document_preview"),

    url(r'^row/(?P<object_id>[^/]+)$',
        login_required(object_detail),
        {'queryset': Document.objects.all(),
         'template_name': 'document_row.tpl'},
        name="row_info"),

    url(r'^edit/(?P<object_id>[^/]+)$',
        AR(login_required(object_detail)),
        {'queryset': Document.objects.all(),
         'template_name': 'document_edit.tpl'},
        name="document_edit"),

    url(r'^desc/(?P<object_id>[^/]+)$',
        AR(login_required(object_detail)),
        {'queryset': Document.objects.all(),
         'template_name': 'document_desc.tpl'},
        name="document_desc"),

    url(r'^post_ed/(?P<id>[^/]+)$',
        require_POST(login_required(edit_post)),
        name="edit_post"),

    url(r'^put/(?P<slug>[^/]+)$', 
        require_POST(login_required(upload_file)), 
        name="upload_file"),

    url(r'^r/(?P<id>\d+)/.*', 
        login_required(download_file), 
        name="download_file"),

    url(r'^i/(?P<pid>\d+)$', 
        login_required(download_page), 
        name="download_page"),

    url(r'^v/(?P<object_id>\d+)/$', 
        AR(login_required(object_detail)), 
        {'queryset': Document.objects.all(), 
         'template_name': 'viewer.tpl'},
        name='view_file'),
)
