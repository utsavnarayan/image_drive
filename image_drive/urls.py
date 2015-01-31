from django.conf.urls import patterns, include, url
from django.contrib import admin
import image_drive, gallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'image_drive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', image_drive.views.index),
    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/logout/$', 'image_drive.views.logout'),
    url('^download/(?P<image_key>[A-Za-z0-9_-]+)/$', image_drive.views.download, name='download'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = image_drive.views.show_error_403
handler404 = image_drive.views.show_error_404
handler500 = image_drive.views.show_error_500