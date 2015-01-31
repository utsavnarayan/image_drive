from gallery.models import Upload

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


def download(request, image_key):
    image = Upload.objects.all().filter(image_key=image_key, user=request.user.id)
    if not image:
        return _show_error(request, "Image not present")
    else:
        from django_downloadview import ObjectDownloadView
        img = ObjectDownloadView.as_view(model=Upload, file_field='pic', attachment=False)
        return img(request, pk=image_key)


def delete(request, image_key):
    image = Upload.objects.all().filter(image_key=image_key, user=request.user.id)
    if not image:
        return _show_error(request, "Image not present")
    else:
        image.delete()
        return HttpResponseRedirect('/')


def _show_error(request, error_code):
    context = RequestContext(request, {
        'error_code': error_code,
    })
    return render_to_response('error.html', context)


def show_error_403(request):
    return _show_error(request, 403)


def show_error_404(request):
    return _show_error(request, 404)


def show_error_500(request):
    return _show_error(request, 500)



