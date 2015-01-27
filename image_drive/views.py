__author__ = 'utsav'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import Template, RequestContext
from forms import MyRegistrationForm


def index(request):
    """""
    Although this logic is little complex but
    it keeps the login/logout/invalid-login views to the same url i.e '/'
    """""
    index_page = 'index.html'
    if request.user.is_authenticated():
        return render_to_response('home.html', context_instance=RequestContext(request))
    form = MyRegistrationForm()
    # Username and password submitted
    if request.method == 'POST':
        if 'Login' in request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            if username and password:
                user = auth.authenticate(username=username, password=password)

                # Successfully logged in
                if user is not None:
                    auth.login(request, user)
                    return render_to_response('home.html', context_instance=RequestContext(request))

                # Incorrect username password combination
                else:
                    return render_to_response('invalid_login.html', context_instance=RequestContext(request))
        elif 'Signup' in request.POST:
            form = MyRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return render_to_response('register_success.html', context_instance=RequestContext(request))

    # Either Login button not clicked or username/password left blank
    args = {}
    args['form'] = form
    args.update(csrf(request))
    return render_to_response(index_page, args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
