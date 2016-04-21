# encoding: utf-8
from django.db import models


class Block(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    number = models.IntegerField(verbose_name='Number', unique=True)
    code = models.CharField(verbose_name='Code', max_length=6, unique=True)

    class Meta:
        db_table = 'block'

    def __str__(self):
        return self.name


