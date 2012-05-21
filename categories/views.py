# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from categories.models import NewCategoryForm, EditCategoryForm, Category
from django.utils.html import escape
from utils.json import json_sublist_send
from courses.models import Course

def new_category(request):
    form = NewCategoryForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cat = Category.objects.create(name=escape(data['name']), 
                                      description=escape(data['description']))
        return HttpResponse("ok " + str(cat.id))
    return HttpResponse("Error: Invalid form")

def edit_category(request):
    form = EditCategoryForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cat = get_object_or_404(Category, pk=data['id'])
        cat.name = escape(data['name'])
        cat.description = escape(data['description'])
        cat.save()
        return HttpResponse("ok")
    return HttpResponse("Error: Invalid form")

def sub_categories(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist_send(request, cat.holds.all, ['id', 'name', 'description'])

def sub_courses(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist_send(request, cat.contains.all, ['id', 'name', 'slug'])

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
        return HttpResponse('This category is not empty, please empty it first', 'text/html')

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
