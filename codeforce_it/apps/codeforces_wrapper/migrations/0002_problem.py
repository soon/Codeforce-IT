# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforces_wrapper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('cf_contest_id', models.IntegerField(verbose_name='Codeforces contest number')),
                ('cf_index', models.CharField(max_length=16, verbose_name='Codeforces problem index')),
                ('max_score', models.FloatField(verbose_name='Maximum amount of points')),
            ],
        ),
    ]
