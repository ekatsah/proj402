from django.shortcuts import render_to_response
from notifications.models import Event
from utils.json import json_sublist_send
from django.db.models import Q

def prep_queryset(request):
    query = Event.objects.order_by("-date")

    q_object = None
    for course in request.REQUEST.get('courses', '').split(' '):
        try:
            course = Course.objects.get(slug=course)
        except:
            continue
        if q_object:
            q_object |= Q(context=course)
        else:
            q_object = Q(context=course)
    if q_object:
        query = query.filter(q_object)
        q_object = None

    for t in request.REQUEST.get('types', '').split(' '):
        if t != '':
            if q_object:
                q_object |= Q(type=t)
            else:
                q_object = Q(type=t)
    if q_object:
        query = query.filter(q_object)

    try:
        length = min(100, max(1, int(request.REQUEST.get('length', '20'))))
    except:
        length = 20

    return query[:length]

def export_json(request):
    return json_sublist_send(request, prep_queryset(request), 
                             ['id', 'url', '__str__', 'date'])

def export_rss(request):
    query = prep_queryset(request)
    return render_to_response('feeds.tpl', {'events': query})
