from django.conf.urls.defaults import *

from django.views.generic.simple import redirect_to

urlpatterns = patterns('tc.views',
    (r'^$', 'index'),
    ('^cs/$', redirect_to, {'url': '/'}),
)
