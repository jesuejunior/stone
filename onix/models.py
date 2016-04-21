# encoding: utf-8
from django.db import models


class Material(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    origin = models.CharField(verbose_name='Origin', max_length=100)

    class Meta:
        db_table = 'material'

    def __str__(self):
        return self.name


class Block(models.Model):
    material = models.ForeignKey(Material, verbose_name='Material')
    number = models.IntegerField(verbose_name='Number', unique=True)
    code = models.CharField(verbose_name='Code', max_length=6, unique=True)

    class Meta:
        db_table = 'block'

    def __str__(self):
        return self.name


