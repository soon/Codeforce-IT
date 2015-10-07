# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('codeforces_wrapper', '0004_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='contest',
            field=models.ForeignKey(to='codeforces_wrapper.Contest', null=True),
        ),
    ]
