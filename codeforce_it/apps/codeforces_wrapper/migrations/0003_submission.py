# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforces_wrapper', '0002_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cf_id', models.IntegerField(verbose_name='Codeforces Id')),
                ('creation_time', models.DateTimeField(verbose_name='Creation time')),
                ('verdict', models.CharField(max_length=3, verbose_name='Verdict', choices=[('FAI', 'Failed'), ('OK', 'OK'), ('PRT', 'Partial'), ('CE', 'Compilation error'), ('RE', 'Runtime error'), ('WA', 'Wrong answer'), ('PE', 'Representation error'), ('TL', 'Time limit exceeded'), ('ML', 'Memory limit exceeded'), ('IL', 'Idleness limit exceeded'), ('SV', 'Security violated'), ('CR', 'Crashed'), ('IPC', 'Input preparation crashed'), ('CLG', 'Challenged'), ('SKP', 'Skipped'), ('TST', 'Testing'), ('REJ', 'Rejected')])),
                ('author', models.ForeignKey(to='codeforces_wrapper.Contestant')),
                ('problem', models.ForeignKey(to='codeforces_wrapper.Problem')),
            ],
        ),
    ]
