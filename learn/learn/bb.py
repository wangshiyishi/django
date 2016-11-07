from django.db import models
from test.test_imageop import MAX_LEN
from django.contrib.auth.models import User

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    rangking = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name= models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBs_user')

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=189,default='This gay is to lazy to levave anything here.')
    photo =models.ImageField()
    photo= models.ImageField(upload_to="upload_imgs/" , default="upload_imgs/user-1.jpg")

    def __unicode__(self):
        return self.title