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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=100)),
                ('number', models.IntegerField(unique=True, verbose_name='Number')),
                ('code', models.CharField(unique=True, verbose_name='Code', max_length=6)),
            ],
            options={
                'db_table': 'block',
            },
        ),
    ]
