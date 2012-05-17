from courses.models import Course, NewCourseForm
from django.http import HttpResponse

def new_course(request):
    form = NewCourseForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data;
        try:
            slug = data['slug'].lower()
            course = Course.objects.create(slug=slug, name=data['name'],
                                           description=data['description'])
            return HttpResponse("ok")
        except:
            HttpResponse("Error: Invalid slug")
    return HttpResponse("Error: Invalid form")
