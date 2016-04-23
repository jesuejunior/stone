# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('number', models.IntegerField(verbose_name='Number', unique=True)),
                ('code', models.CharField(verbose_name='Code', max_length=6, unique=True)),
            ],
            options={
                'db_table': 'block',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('origin', models.CharField(verbose_name='Origin', max_length=100)),
            ],
            options={
                'db_table': 'material',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='material',
            field=models.ForeignKey(to='onix.Material', verbose_name='Material'),
        ),
    ]
