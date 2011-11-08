from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from upload.models import UploadFileForm
from django.core.urlresolvers import reverse

def upload_file(request, slug):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pass
            # the file is in request.FILES['file']

    # FIXME add an error management
    return HttpResponseRedirect(reverse('course_show', args=[slug]))
