# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-11-27 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0002_auto_20201124_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='name',
            new_name='profname',
        ),
    ]