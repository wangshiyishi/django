from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'learn.views.index'),  # new
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
# coding:utf-8
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
python manage.py startapp learn # learn 是一个app的名称
django-admin startproject mysite

采用 /add/?a=4&b=5 这样GET方法进行

django-admin.py startproject zqxt_views
cd zqxt_views
python manage.py startapp calc

采用 /add/?a=4&b=5 这样GET方法进行

django-admin.py startproject zqxt_views
cd zqxt_views
python manage.py startapp calc

from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^add/$', 'clac.views.add', name='add'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))

采用 /add/3/4/

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

url(r'^add/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),

跳转

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


url(r'^add/(\d+)/(\d+)/$', calc_views.old_add2_redirect),
url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),

模板
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'learn.views.home', name='home'),  # new
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>欢迎光临</title>
</head>
<body>
欢迎光临天堂
</body>
</html>

def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})
html：
教程列表：
{% for i in TutorialList %}
{{ i }}
{% endfor %}

def home(request):
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'home.html', {'info_dict': info_dict}
    站点：{{info_dict.site}}内容：{{ info_dict.content }} or
    { %for key, value in info_dict.items %}
    {{key}}: {{value}}
    { % endfor %}

    def home(request):
        List = map(str, range(100))  # 一个长度为100的 List
        return render(request, 'home.html', {'List': List})
{% for item in List %}
    {{ item }}{% if not forloop.last%},{% endif %}
{% endfor %}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)


<a href="{{ request.path }}?{{ request.GET.urlencode }}&delete=1">当前网址加参数 delete</

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self.name
