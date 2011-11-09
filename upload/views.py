from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from upload.models import UploadFileForm, Document
from django.core.urlresolvers import reverse
from courses.models import Course
from settings import UPLOAD_DIR

def upload_file(request, slug):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            course = get_object_or_404(Course, slug=slug)
            d = Document.new(request.user, course, request.FILES['file'])
            course.add_document(d)
            
    # FIXME add an error management
    return HttpResponseRedirect(reverse('course_show', args=[slug]))

def download_file(request, id):
    document = get_object_or_404(Document, pk=id)
    response = HttpResponse(document.get_content(), mimetype="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=' + document.name
    return response

def download_page(request, doc_id, num):
    # check for input!!
    f = open(UPLOAD_DIR + '/doc_%03d_%04d.png' % (int(doc_id), int(num)), 'r')
    data = f.read()
    f.close()
    return HttpResponse(data, mimetype="image/png")