from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'learn.views.index'),  # new
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
