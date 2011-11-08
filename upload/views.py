from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from upload.models import UploadFileForm, Document
from django.core.urlresolvers import reverse
from courses.models import Course

def upload_file(request, slug):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            course = get_object_or_404(Course, slug=slug)
            d = Document.new(request.user, course, request.FILES['file'])
            course.add_document(d)
            
    # FIXME add an error management
    return HttpResponseRedirect(reverse('course_show', args=[slug]))
