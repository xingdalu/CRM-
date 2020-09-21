from django.db import models


# Create your models here.
class Permission(models.Model):
    # 权限表
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的url', max_length=132)

    def __str__(self):
        return self.title


class Role(models.Model):
    # 角色
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to=Permission, blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    # 用户表
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=100)
    email = models.CharField(verbose_name='邮箱', max_length=100)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to=Role, blank=True)

    def __str__(self):
        return self.name
