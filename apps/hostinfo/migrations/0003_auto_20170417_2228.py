# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0002_hostgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name': '\u4e3b\u673a\u5217\u8868', 'verbose_name_plural': '\u4e3b\u673a\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='hostgroup',
            options={'verbose_name': '\u4e3b\u673a\u7ec4', 'verbose_name_plural': '\u4e3b\u673a\u7ec4'},
        ),
    ]
