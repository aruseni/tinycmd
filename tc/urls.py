from django.conf.urls.defaults import *

from django.views.generic.simple import redirect_to

urlpatterns = patterns('tc.views',
    (r'^$', 'index'),
    (r'^post/$', 'add_command_string'),
    (r'^cs/(?P<command_string_id>\w+)/$', 'command_string_detail'),
    (r'^cs/(?P<command_string_id>\w+)/text/$', 'command_string_text'),
    (r'^cs/$', redirect_to, {'url': '/'}),
)
