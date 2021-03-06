# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed


class User(AbstractUser):
    email = models.EmailField(verbose_name="电子邮箱", unique=True, default='test')
    name = models.CharField(max_length=255, verbose_name="姓名", default='test')
    student_id = models.CharField(max_length=255, verbose_name="学号", default='test')
    school = models.CharField(max_length=255, verbose_name="学院", default='test')
    gender = models.CharField(max_length=1, verbose_name="性别", default='test')
    is_activate = models.BooleanField(verbose_name="是否允许选择", default=False)


class Site(models.Model):
    location = models.CharField(max_length=255, verbose_name="地点")
    time = models.CharField(max_length=255, verbose_name="时间")
    capacity = models.IntegerField(verbose_name="可选人数")
    students = models.ManyToManyField(User)


# ref: https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield/20230270
def students_changed(sender, **kwargs):
    if kwargs['instance'] in Site.objects.all():
        if kwargs['instance'].students.count() > kwargs['instance'].capacity:
            raise ValidationError("The site is already full")
    else:
        pass


m2m_changed.connect(students_changed, sender=Site.students.through)
