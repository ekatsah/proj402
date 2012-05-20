# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from courses.models import Course, NewCourseForm
from django.http import HttpResponse
from django.utils.html import escape

def new_course(request):
    form = NewCourseForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        try:
            slug = data['slug'].lower()
            course = Course.objects.create(slug=slug, escape(name=data['name']),
                                        description=escape(data['description']))
            return HttpResponse("ok")
        except:
            HttpResponse("Error: Invalid slug")
    return HttpResponse("Error: Invalid form")
