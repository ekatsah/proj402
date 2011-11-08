from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from upload.models import UploadFileForm
from upload.views import upload_file

urlpatterns = patterns('users.views',
    url(r'^get$', login_required(direct_to_template), 
        {'template': 'upload_form.tpl', 
         'extra_context': {'form': UploadFileForm()}}, 
        name="upload_form"),
    url(r'^put/(?P<slug>[^/]+)$', login_required(upload_file), name="upload_file"),
)
