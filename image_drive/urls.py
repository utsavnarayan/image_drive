from django.conf.urls import patterns, include, url
from django.contrib import admin
import image_drive

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'image_drive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', image_drive.views.index),
    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/logout/$', 'image_drive.views.logout'),
)

