from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from courses.models import Course, Category

def catadd(request, category, subcategory):
    cat = get_object_or_404(Category, pk=category)
    subcat = get_object_or_404(Category, pk=subcategory)
    cat.holds.add(subcat)
    return HttpResponse('ok', 'text/html')

def catnew(request, category, name):
    cat = get_object_or_404(Category, pk=category)
    subcat = Category(name=name, description=".")
    subcat.save();
    cat.holds.add(subcat)
    return HttpResponse('ok', 'text/html')

def catrm(request, category, parent):
    cat = get_object_or_404(Category, pk=category)
    supercat = get_object_or_404(Category, pk=parent)
    supercat.holds.remove(cat)
    return HttpResponse('ok', 'text/html')
