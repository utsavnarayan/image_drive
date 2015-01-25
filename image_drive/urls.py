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
    url(r'^accounts/auth/$',  'image_drive.views.auth_view'),
    url(r'^accounts/logout/$', 'image_drive.views.logout'),
    url(r'^accounts/loggedin/$', 'image_drive.views.loggedin'),
    url(r'^accounts/invalid/$', 'image_drive.views.invalid_login'),
    url(r'^accounts/register/$', 'image_drive.views.register_user'),
    url(r'^accounts/register_success/$', 'image_drive.views.register_success'),
)

