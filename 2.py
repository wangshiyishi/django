# coding:utf-8
from django.db import models


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    from django.contrib import admin
    from .models import Article

    admin.site.register(Article)

    class Person(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)

        def my_property(self):
            return self.first_name + ' ' + self.last_name

        my_property.short_description = "Full name of the person"

        full_name = property(my_property)

        from django.contrib import admin
        from .models import Article, Person

        class ArticleAdmin(admin.ModelAdmin):
            list_display = ('title', 'pub_date', 'update_time',)

        class PersonAdmin(admin.ModelAdmin):
            list_display = ('full_name',)

        admin.site.register(Article, ArticleAdmin)
        admin.site.register(Person, PersonAdmin)

        class MyModelAdmin(admin.ModelAdmin):
            def get_queryset(self, request):
                qs = super(MyModelAdmin, self).get_queryset(request)
                if request.user.is_superuser:
                    return qs
                else:
                    return qs.filter(author=request.user)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct


from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:  # 新增的时候
            obj_original = None

        obj.user = request.user
        obj.save()


from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        # handle something here
        obj.delete()


# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from .forms import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
<form method='post'>
{% csrf_token %}
{{ form }}
<input type="submit" value="提交">
</form>


from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(' ' ,
      # 注意下面这一行
      url(r'^$', 'tools.views.index', name='home'),
      url(r'^admin/', include(admin.site.urls)),
)





