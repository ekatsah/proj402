from django.http import HttpResponse
from django.core import serializers

def json_list(request, queryset):
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, 'application/javascript')
