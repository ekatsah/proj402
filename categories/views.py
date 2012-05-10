from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from categories.models import NewCategoryForm, Category
from utils.json import json_sublist
from courses.models import Course

def new_category(request):
    form = NewCategoryForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data;
        cat = Category.objects.create(name=data['name'], 
                                      description=data['description'])
        return HttpResponse("ok " + str(cat.id))
    return HttpResponse("Error: Invalid form")

def sub_categories(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist(request, cat.holds.all, ['id', 'name', 'description'])

def sub_courses(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist(request, cat.contains.all, ['id', 'name', 'slug'])

def attach_category(request, category, subcategory):
    cat = get_object_or_404(Category, pk=category)
    subcat = get_object_or_404(Category, pk=subcategory)
    cat.holds.add(subcat)
    return HttpResponse('ok', 'text/html')

def detach_category(request, category, parent):
    cat = get_object_or_404(Category, pk=category)
    supercat = get_object_or_404(Category, pk=parent)
    supercat.holds.remove(cat)
    return HttpResponse('ok', 'text/html')

def del_category(request, category):
    cat = get_object_or_404(Category, pk=category)
    if len(cat.contains.all()) == 0 and len(cat.holds.all()) == 0:
        cat.delete()
        return HttpResponse('ok', 'text/html')
    else:
        return HttpResponse('not empty object', 'text/html')

def attach_course(request, category, slug):
    cat = get_object_or_404(Category, pk=category)
    course = get_object_or_404(Course, slug=slug)
    cat.contains.add(course)
    return HttpResponse('ok', 'text/html')

def detach_course(request, category, slug):
    cat = get_object_or_404(Category, pk=category)
    course = get_object_or_404(Course, slug=slug)
    cat.contains.remove(course)
    return HttpResponse('ok', 'text/html')
