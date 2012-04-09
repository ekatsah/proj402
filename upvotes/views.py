from documents.models import Document
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from upvotes.models import VoteHistory, CAT_DOCUMENTS

def vote_doc(request, id, category, score):
    doc = get_object_or_404(Document, pk=id)
    # add points and cat
    return HttpResponse('ok', 'text/html')