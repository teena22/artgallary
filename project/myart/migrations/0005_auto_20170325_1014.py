# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-25 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myart', '0004_paintings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paintings',
            new_name='Painting',
        ),
    ]