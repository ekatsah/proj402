from django.http import HttpResponse
from django.core import serializers
from django.db.models.manager import Manager

def json_list(request, queryset):
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, 'application/javascript')

def json_sublist(request, queryset, fields):
    objects = []
    for o in queryset():
        object_str = []
        for f in fields:
            attr = getattr(o, f)
            if type(attr) == unicode:
                object_str.append('"%s": "%s"' % (f, attr))
            elif type(attr) == int:
                object_str.append('"%s": "%d"' % (f, attr))
            elif attr is None:
                continue
            else:
                l = []
                for i in attr.all():
                    l.append(str(i.id))
                object_str.append('"%s": [%s]' % (f, ",".join(l)))
        objects.append("{" + ",".join(object_str) + "}")
    return HttpResponse("[" + ",".join(objects) + "]", 'application/javascript')
