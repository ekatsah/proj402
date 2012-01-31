from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from utils.decorators import AR

urlpatterns = patterns('users.views',
    url(r'^$', AR(login_required(direct_to_template)), 
        {'template': 'user_show.tpl'}, name='profile'),

    url(r'^login/$', login, {'template_name': 'user_login.tpl'}, name="user_login"),
    url(r'^logout/$', logout, {'next_page': '/'}, name="user_logout"),
)
