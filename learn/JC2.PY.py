django-admin stratproject mysite
python manage.py starapp learn

# coding:utf-8
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'learn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

