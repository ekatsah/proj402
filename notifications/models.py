# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

action_fields, output_method = dict(), dict()

def check_field(name, value):
    if name in action_fields:
        if isinstance(value, models.ForeignKey):
            if action_fields[name].rel.to != value.rel.to:
                raise Exception("Action model error, ForeignKey %s incoherent" % name)
        elif action_fields[name] != value:
            raise Exception("Action model error, value %s incoherent" % name)
        elif name == "type" or name == "date":
            raise Exception("Action model error, name %s forbidden" % name)
    else:
        return True

def create_event():
    class Meta:
        app_label = 'notifications'

    def to_string(self):
        return self._output[self.type](self)

    action_fields['Meta'] = Meta
    action_fields['type'] = models.CharField(max_length=100)
    action_fields['date'] = models.DateTimeField(default=datetime.now)
    action_fields['_output'] = output_method
    action_fields['__module__'] = 'notifications'
    action_fields['__str__'] = to_string
    action_fields['__unicode__'] = to_string
    
    return type('Event', (models.Model,), action_fields)

class MetaEvent(type):
    def __init__(cls, name, bases, dict):
        for attr, value in dict.iteritems():
            if attr.startswith('__'):
                continue
            if check_field(attr, value):
                action_fields[attr] = value
        
        output_method[cls.__name__] = dict['__str__']

class BaseEvent(object):
    @classmethod
    def throw(cls, *args, **kwargs):
        event = Event(*args, **kwargs)
        event.type = cls.__name__
        event.save()
        return event

Event = create_event()
