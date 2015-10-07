# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('codeforces_wrapper', '0007_auto_20150928_0642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='problem',
            unique_together=set([('cf_contest_id', 'cf_index', 'contest')]),
        ),
    ]
