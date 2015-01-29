__author__ = 'utsav'
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from forms import MyRegistrationForm


def index(request):
    """""
    The implementation of this view allows to keep the url same '/'
    for all scenarios (login/logout/register/gallery pages)

    Note: Ideally front-end frameworks like angular js should be used
    and these views should only function as REST API returning JSON data
    """""
    if request.user.is_authenticated():
        return home(request)
    elif request.method == 'POST':
        if 'Login' in request.POST:
            return auth_user(request)
        elif 'Signup' in request.POST:
            return register(request)
    else:
        return default(request)


def auth_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if username and password:
        user = auth.authenticate(username=username, password=password)
        # Successfully logged in
        if user is not None:
            auth.login(request, user)
            return home(request)
        # Incorrect username password combination
        else:
            return invalid_login(request)


def invalid_login(request):
    return render_to_response('invalid_login.html', context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    form = MyRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return render_to_response('register_success.html', context_instance=RequestContext(request))
    else:
        return render_to_response('register_failed.html', {'form': form}, context_instance=RequestContext(request))


def default(request):
    args = {}
    args['form'] = MyRegistrationForm()
    args.update(csrf(request))
    return render_to_response('index.html', args)


def home(request):
    from gallery.models import Upload
    from gallery.forms import UploadForm
    if request.method == "POST" and 'Upload' in request.POST:
            img = UploadForm(request.POST, request.FILES)
            if img.is_valid():
                img.save(user=request.user)
                return HttpResponseRedirect('/')
    else:
        img = UploadForm()
    images = Upload.objects.all().filter(user=request.user)
    return render(request, 'home.html', {'form': img, 'images': images})
