from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from upload.models import UploadFileForm
from upload.views import upload_file, download_file, download_page

urlpatterns = patterns('users.views',
    url(r'^get$', login_required(direct_to_template), 
        {'template': 'upload_form.tpl', 
         'extra_context': {'form': UploadFileForm()}}, 
        name="upload_form"),
    url(r'^put/(?P<slug>[^/]+)$', login_required(upload_file), name="upload_file"),
    url(r'^r/(?P<id>\d+)/.*', login_required(download_file), name="download_file"),
    url(r'^i/(?P<doc_id>\d+)/(?P<num>\d+)$', login_required(download_page), 
        name="download_page"),
)
