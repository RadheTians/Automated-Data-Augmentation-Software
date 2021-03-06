from django.urls import path, re_path

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello.views.index, name="index"),
    path("upload", hello.views.Upload, name="index"),
    path("multiImage", hello.views.Multi_Images, name="multiImage"),
    re_path(r'^.*Unread.*',hello.views.Unread,name='Unread')
]
