# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20160530_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(to='taskmanager.Profile', related_name='tags', verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'ordering': ('user', 'name'),
                'verbose_name': 'Tag',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('user', 'name')]),
        ),
    ]
