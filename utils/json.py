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

def json_string(value):
    table = {'\\': '\\u005C', '"': '\\u0022', '/': '\\u002F', '\b': '\\u0008',
             '\f': '\\u000C', '\n': '\\u000A', '\r': '\\u000D', '\t': '\\u009'}
    return ''.join([ table.get(v, v) for v in value ])

def json_object(obj, fields):
    def get_recur_attr(obj, attrs):
        attr = attrs.pop(0)
        val = getattr(obj, attr, None)
        if callable(val):
                val = val()
        if len(attrs) > 0:
            return get_recur_attr(val, attrs)
        else:
            return val

    object_str = []
    for field in fields:
        value = get_recur_attr(obj, field.split('.'))

        if value is None:
            object_str.append('"%s": null' % field)

        elif type(value) == bool:
            object_str.append('"%s": %s' % (field, str(value).lower()))

        elif type(value) == unicode or type(value) == str:
            object_str.append('"%s": "%s"' % (field, json_string(value)))

        elif type(value) == int:
            object_str.append('"%s": "%d"' % (field, value))

        elif isinstance(value, datetime):
            object_str.append('"%s": "%s"' % 
                              (field, value.strftime("%d/%m/%y %H:%M")))

        elif value.__class__.__name__ == 'ManyRelatedManager':
            ids = [ str(x.id) for x in value.all() ]
            object_str.append('"%s": [%s]' % (field, ",".join(ids)))

    return "{" + ",".join(object_str) + "}"

def json_sublist(queryset, fields):
    queryset = queryset() if callable(queryset) else queryset
    objects = [ json_object(obj, fields) for obj in queryset ]
    return "[" + ",".join(objects) + "]"

def json_object_send(request, obj, fields):
    return HttpResponse(json_object(obj, fields), 'application/javascript')

def json_select_send(request, queryset, fields, **kwargs):
    queryset = queryset() if callable(queryset) else queryset
    for k, v in kwargs.iteritems():
        queryset = queryset.filter(**{k: v})

    if (len(queryset)) == 0:
        return HttpResponse('{}', 'application/javascript')
    elif (len(queryset)) == 1:
        return json_object_send(request, queryset[0], fields)
    else:
        return json_sublist_send(request, queryset, fields)

def json_sublist_send(request, queryset, fields):
    return HttpResponse(json_sublist(queryset, fields), 'application/javascript')
