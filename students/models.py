# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"

    student_group = models.ForeignKey('Group',
                                      verbose_name=u"Група",
                                      blank=False,
                                      null=True,
                                      on_delete=models.PROTECT
                                      )

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я")
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По-батькові",
        default='')
    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True)
    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)
    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет")
    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")
    leader = models.OneToOneField(
        'Student',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=u"Староста")
    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __str__(self):
        if self.leader:
            return u'%s(%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u'%s' % self.title

    def __unicode__(self):
        if self.leader:
            return u'%s(%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u'%s' % self.title
