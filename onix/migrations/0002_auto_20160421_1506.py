# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=100),
        ),
    ]
