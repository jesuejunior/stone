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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
            field=models.ForeignKey(verbose_name='Material', to='onix.Material'),
        ),
    ]
