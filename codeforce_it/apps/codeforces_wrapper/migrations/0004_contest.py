# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforces_wrapper', '0003_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('contestants', models.ManyToManyField(to='codeforces_wrapper.Contestant')),
            ],
        ),
    ]
