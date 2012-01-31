from utils.json import json_sublist
from courses.models import Category
from django.shortcuts import get_object_or_404

def subcategory(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist(request, cat.holds.all(), ['id', 'name', 'description'])

def courses_by_cat(request, catid):
    cat = get_object_or_404(Category, pk=int(catid))
    return json_sublist(request, cat.contains.all(), ['id', 'name', 'slug'])