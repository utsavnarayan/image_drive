from django.shortcuts import render
from gallery.models import Upload
from gallery.forms import UploadForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def home(request):
    if request.method == "POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img = UploadForm()
    images = Upload.objects.all()
    return render(request, 'home.html', {'form': img, 'images': images})
