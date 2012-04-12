from documents.models import Document
from django.shortcuts import get_object_or_404, render

def search(request):
    if 'q' not in request.GET or request.GET['q'] == '':
        return render(request, 'search.tpl', {'msg': 'You searched nothing!'})
    
    query = request.GET['q'].split()
    return render(request, 'search.tpl', {'msg': 'Keywords : ' + str(query)})