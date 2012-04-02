from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from documents.models import UploadFileForm, Document
from documents.views import upload_file, download_file, download_page
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
         'template_name': 'preview_doc.tpl'},
        name="preview_doc"),

    url(r'^row/(?P<object_id>[^/]+)$',
        login_required(object_detail),
        {'queryset': Document.objects.all(),
         'template_name': 'document_row.tpl'},
        name="row_info"),

    url(r'^put/(?P<slug>[^/]+)$', 
        login_required(upload_file), 
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
