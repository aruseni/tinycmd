# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse

from tc.models import CommandString

def index(request):
    return render_to_response('index.html', {},
                               context_instance=RequestContext(request))

def command_string_detail(request, command_string_id):
    command_string = get_object_or_404(CommandString, string_id=command_string_id)
    return render_to_response('command_string.html', {'command_string': command_string},
                               context_instance=RequestContext(request))

def command_string_text(request, command_string_id):
    command_string = get_object_or_404(CommandString, string_id=command_string_id)
    return HttpResponse(command_string.command_string, mimetype="text/plain")
