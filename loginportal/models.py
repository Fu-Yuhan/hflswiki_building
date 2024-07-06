from django.db import models

# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)

class user(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=32) # 书籍名称
    email = models.CharField(max_length=40) # 书籍价格
    passwordhash = models.CharField(max_length=32) # 出版社名称
    reg_date = models.DateField()
