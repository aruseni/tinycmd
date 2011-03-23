# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from tc.models import CommandString

def index(request):
    return render_to_response('index.html', {},
                               context_instance=RequestContext(request))
