from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from search.views import search

urlpatterns = patterns('search.views', 
    url(r'^s$', 
        login_required(search), 
        name='search_query'),
)
