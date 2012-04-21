from documents.models import Document
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from upvotes.models import VoteHistory, CAT_DOCUMENTS, REF_DOCUMENTS as REFD

def vote_doc(request, id, category, score):
    doc = get_object_or_404(Document, pk=id)
    
    try: 
        score = int(score)
    except:
        return HttpResponse('score not int', 'text/html')

    if score != -1 and score != 1:
        return HttpResponse('bad score value', 'text/html')
    
    try:
        vote = VoteHistory.objects.create(voter=request.user, ressource='D', 
                                          resid=doc.pk, cat=category, 
                                          score=score)
    except:
        return HttpResponse('already in history', 'text/html')

    vote = doc.points
    vote.score += score
    setattr(vote, REFD[category], getattr(vote, REFD[category]) + 1)
    max, max_cat = 0, 'O'
    for cat, attr in REFD.iteritems():
        if max < getattr(vote, attr):
            max, max_cat = getattr(vote, attr), cat
    vote.category = max_cat
    vote.save()
    return HttpResponse('ok', 'text/html')
