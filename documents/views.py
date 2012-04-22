from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from courses.models import Course
from documents.models import UploadFileForm, EditForm, Document, Page
from settings import UPLOAD_DIR

def upload_file(request, slug):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        course = get_object_or_404(Course, slug=slug)
        d = Document.new(request.user, course, request.FILES['file'], 
                         form.cleaned_data['category'])
        course.add_document(d)
            
    # FIXME add an error management
    return HttpResponseRedirect(reverse('course_show', args=[slug]))

def download_file(request, id):
    document = get_object_or_404(Document, pk=id)
    response = HttpResponse(document.get_content(), mimetype="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=' + document.pretty_name()
    return response

def download_page(request, pid=None):
    page = get_object_or_404(Page, pk=pid)
    return HttpResponse(page.get_content(), mimetype="image/png")

def edit_post(request, id):
    doc = get_object_or_404(Document, pk=id)
    form = EditForm(request.POST)
    if form.is_valid():
        doc.name = form.cleaned_data['name']
        doc.description = form.cleaned_data['description']
        doc.save()
    else:
        return HttpResponse('form invalid', 'text/html')
        
    return HttpResponse('ok', 'text/html')
