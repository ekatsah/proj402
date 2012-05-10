from utils.json import json_sublist
from courses.models import Category, Course, NewCourseForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def subcategory(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist(request, cat.holds.all, ['id', 'name', 'description'])

def courses_by_cat(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist(request, cat.contains.all, ['id', 'name', 'slug'])

def new_course(request):
    form = NewCourseForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data;
        try:
            course = Course.objects.create(slug=data['slug'], name=data['name'],
                                           description=data['description'])
            return HttpResponse("ok")
        except:
            HttpResponse("Error: Invalid slug")
    return HttpResponse("Error: Invalid form")

def category_del(request, category):
    cat = get_object_or_404(Category, pk=category)
    if len(cat.contains.all()) == 0 and len(cat.holds.all()) == 0:
        cat.delete()
        return HttpResponse('ok', 'text/html')
    else:
        return HttpResponse('not empty object', 'text/html')

def course_detach(request, course, category):
    cat = get_object_or_404(Category, pk=category)
    cou = get_object_or_404(Course, pk=course)
    cat.contains.remove(cou)
    return HttpResponse('ok', 'text/html')
