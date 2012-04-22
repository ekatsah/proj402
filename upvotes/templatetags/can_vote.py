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
