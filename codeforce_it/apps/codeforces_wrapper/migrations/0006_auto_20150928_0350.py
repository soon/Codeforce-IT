# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('codeforces_wrapper', '0005_problem_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='contestants',
            field=models.ManyToManyField(blank=True, to='codeforces_wrapper.Contestant'),
        ),
    ]
