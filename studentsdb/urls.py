"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from students.views import (students_views,
                            groups_views,
                            journal_views,
                            )
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
                       # students urls
                       url(r'^$', students_views.students_list, name='home'),
                       # students_add
                       url(r'^students/add/$', students_views.students_add,
                           name='students_add'),
                       # students_edit
                       url(r'^students/(?P<sid>\d+)/edit/$',
                           students_views.students_edit,
                           name='students_edit'),
                       # students_delete
                       url(r'^students/(?P<sid>\d+)/delete/$',
                           students_views.students_delete,
                           name='students_delete'),

                       # groups urls
                       url(r'^groups/$', groups_views.groups_list, name='groups'),
                       # groups_add
                       url(r'^groups/add/$', groups_views.groups_add, name='groups_add'),
                       # groups_edit
                       url(r'^groups/(?P<gid>\d+)/edit/$',
                           groups_views.groups_edit,
                           name='groups_edit'),
                       # groups_delete
                       url(r'^groups/(?P<gid>\d+)/delete/$',
                           groups_views.groups_delete,
                           name='groups_delete'),

                       # journal
                       url(r'^journal/$', journal_views.journal, name='journal'),

                       # admin page
                       url(r'^admin/', admin.site.urls),
                       ]

#
# if DEBUG:
#     # serve files from media folder
#     urlpatterns += patterns('',
#                             url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#                                 {'document_root': MEDIA_ROOT}))


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
