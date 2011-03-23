# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def add_command_string(request):
    command_string_string = request.POST.get('command', '')
    if not command_string_string:
        return HttpResponseRedirect(reverse('tc.views.index'))
    command_string = CommandString()
    command_string.command_string = command_string_string
    command_string.save()
    # Reload the object to get the string_id added by the save() method
    command_string = CommandString.objects.get(id=command_string.id)
    return HttpResponseRedirect(reverse('tc.views.command_string_detail', args=(command_string.string_id,)))
