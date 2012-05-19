# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from datetime import datetime
from django.http import HttpResponse
from django.core import serializers
from django.db.models import ManyToManyField

def json_list(request, queryset):
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, 'application/javascript')

def json_sublist(request, queryset, fields):
    def get_recur_attr(obj, attrs):
        attr = attrs.pop(0)
        val = getattr(obj, attr, None)
        if callable(val):
                val = val()
        if len(attrs) > 0:
            return get_recur_attr(val, attrs)
        else:
            return val

    objects = []
    qs = queryset() if callable(queryset) else queryset
    for obj in qs:
        object_str = []
        for field in fields:
            value = get_recur_attr(obj, field.split('.'))

            if type(value) == unicode or type(value) == str:
                object_str.append('"%s": "%s"' % 
                                  (field, value.replace('"', '\\"')))

            elif type(value) == int:
                object_str.append('"%s": "%d"' % (field, value))

            elif isinstance(value, datetime):
                object_str.append('"%s": "%s"' % 
                                  (field, value.strftime("%d/%m/%y %H:%M")))

            elif value.__class__.__name__ == 'ManyRelatedManager':
                ids = [ str(x.id) for x in value.all() ]
                object_str.append('"%s": [%s]' % (field, ",".join(ids)))

        objects.append("{" + ",".join(object_str) + "}")
    return HttpResponse("[" + ",".join(objects) + "]", 'application/javascript')
