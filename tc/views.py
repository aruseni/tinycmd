# Create your views here.


from django.contrib import auth
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from tc.models import CommandString


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def index(request):
    return render_to_response('index.html', {},
                               context_instance=RequestContext(request))

def command_string_detail(request, command_string_id):
    command_string = get_object_or_404(CommandString, string_id=command_string_id,
                                       user_added=None)
    return render_to_response('command_string.html', {'command_string': command_string},
                               context_instance=RequestContext(request))

def user_command_string_detail(request, username, command_string_id):
    command_string = get_object_or_404(CommandString, string_id=command_string_id,
                                       user_added=User.objects.get(username=username))
    return render_to_response('command_string.html', {'command_string': command_string},
                               context_instance=RequestContext(request))

def command_string_text(request, command_string_id):
    command_string = get_object_or_404(CommandString, string_id=command_string_id,
                                       user_added=None)
    return HttpResponse(command_string.command_string, mimetype="text/plain")

def user_command_string_text(request, username, command_string_id):
    command_string = get_object_or_404(CommandString, string_id=command_string_id,
                                       user_added=User.objects.get(username=username))
    return HttpResponse(command_string.command_string, mimetype="text/plain")

def add_command_string(request):
    command_string_string = request.POST.get('command', '')
    try:
        command_string = CommandString.objects.get(command_string=command_string_string, 
                                                   user_added=request.user if \
                                                   request.user.is_authenticated() else None)
    except CommandString.DoesNotExist:
        cmdid = request.POST.get('cmdid', '')
        try:
            command_string = CommandString.objects.get(string_id=cmdid, 
                                                       user_added=request.user \
                                                       if request.user.is_authenticated() else None)
        except CommandString.DoesNotExist:
            if not command_string_string:
                return HttpResponseRedirect(reverse('tc.views.index'))
            command_string = CommandString()
            command_string.command_string = command_string_string
            if request.user.is_authenticated():
                command_string.user_added = request.user
                command_string.string_id = cmdid
            command_string.save()
            # Reload the object to get the string_id added by the save() method
            command_string = CommandString.objects.get(id=command_string.id)
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('tc.views.user_command_string_detail', 
                                            args=(request.user.username,
                                                  command_string.string_id,)))
    else:
        return HttpResponseRedirect(reverse('tc.views.command_string_detail', 
                                            args=(command_string.string_id,)))
        

def command_list(request):
    cmdlist = CommandString.objects.order_by('-datetime_added')
    return render_to_response('command_list.html', {'cmdlist': cmdlist}, 
                              context_instance=RequestContext(request))

def user_command_list(request, username):
    user = User.objects.get(username=username)
    cmdlist = CommandString.objects.filter(user_added=user).order_by('-datetime_added')
    return render_to_response('command_list.html', {'cmdlist': cmdlist}, 
                              context_instance=RequestContext(request))

def command_list_text(request):
    cmdlist = CommandString.objects.order_by('-datetime_added')
    return HttpResponse('\n'.join(map(lambda s: s.string_id, cmdlist)))

def user_command_list_text(request, username):
    user = User.objects.get(username=username)
    cmdlist = CommandString.objects.filter(user_added=user).order_by('-datetime_added')
    return HttpResponse('\n'.join(map(lambda s: s.string_id, cmdlist)))

