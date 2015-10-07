# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('codeforces_wrapper', '0006_auto_20150928_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='cf_id',
            field=models.IntegerField(unique=True, verbose_name='Codeforces Id'),
        ),
    ]
