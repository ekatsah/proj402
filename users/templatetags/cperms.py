# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

from django import template

register = template.Library()

@register.filter()
def has_perm(args, perm):
    if isinstance(args, list):
        return args[0].profile.has_perm(perm, args[1])
    else:
        return args.profile.has_perm(perm)

@register.filter()
def attach(first, obj):
    if isinstance(first, list):
        return first + [obj]
    else:
        return [first , obj]
