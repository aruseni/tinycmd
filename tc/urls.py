from django.conf.urls.defaults import *

from django.views.generic.simple import redirect_to

urlpatterns = patterns('tc.views',
    (r'^$', 'index'),
    (r'^post/$', 'add_command_string'),
    (r'^(?P<username>[\w\d_]+)/cs/(?P<command_string_id>\w+)/$', 
     'user_command_string_detail'),
    (r'^cs/(?P<command_string_id>\w+)/$', 'command_string_detail'),
    (r'^(?P<username>[\w\d_]+)/cs/(?P<command_string_id>\w+)/text/$', 
     'user_command_string_text'),
    (r'^cs/(?P<command_string_id>\w+)/text/$', 'command_string_text'),
    (r'^(?P<username>[\w\d_]+)/cs/$', redirect_to, {'url': '/'}),
    (r'^cs/$', redirect_to, {'url': '/'}),
    (r'^accounts/login/$',  'login'),
    (r'^accounts/logout/$', 'logout'),
    (r'^list/text/$', 'command_list_text'),
    (r'^list/$', 'command_list'),
    (r'^(?P<username>[\w\d_]+)/list/text/$', 'user_command_list_text'),
    (r'^(?P<username>[\w\d_]+)/list/$', 'user_command_list'),
)
