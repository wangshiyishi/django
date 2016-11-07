from  django.contrib import admin
from app01 import models

admin.site.register(models.BBS)
admin.site.register(models.Category)
admin.site.register(models.BBs_user)