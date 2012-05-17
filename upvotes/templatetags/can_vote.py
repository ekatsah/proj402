# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.
from django import template
from upvotes.models import VoteHistory

def can_vote(user, doc, res):
    objs = VoteHistory.objects.filter(voter=user)
    objs = objs.filter(ressource=res).filter(resid=doc.id)
    return len(objs) == 0

register = template.Library()

@register.filter()
def can_voteD(user, doc):
    return can_vote(user, doc, 'D')
