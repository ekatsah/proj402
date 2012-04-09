from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from upvotes.views import vote_doc

urlpatterns = patterns('upvotes.views', 
    url(r'^doc/(?P<id>\d+)/(?P<category>[ROSEPLD])/(?P<score>[-1]+)$', 
        login_required(vote_doc), 
        name='vote_doc'),
)
