from  django.contrib import admin
from app import models


class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author',' signature', 'view_count', 'cerated_at' )
    list_filter = ('created_at',)
    search_fields = ('title','author__user__username')
    def signature(self,obj):
        return obj.author. signature
     signature.shortDescription = 'HAA'

admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBs_user)