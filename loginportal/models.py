from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

#class Test(models.Model):
#    name = models.CharField(max_length=20)

class UserExtra(models.Model):
    id = models.AutoField(primary_key=True)
    BaseInfo = models.OneToOneField(User, on_delete=models.CASCADE)
    sth_to_say = models.CharField(max_length=50, null=True)
    level = models.IntegerField(null=True)
    coin = models.IntegerField(null=True)
    #followers = models.ManyToManyField("self", related_name="followed_by", blank=True)
    #followed_by = models.ManyToManyField("self", related_name="followers", blank=True)
    type = models.CharField(max_length=20, null=True)
    #    avatar = models.ImageField(upload_to='images/', null=True)
