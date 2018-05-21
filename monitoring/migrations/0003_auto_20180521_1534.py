# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20180521_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbffile',
            old_name='file',
            new_name='file1',
        ),
        migrations.RenameField(
            model_name='dbffile',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='dbffile',
            name='file2',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dbffile',
            name='title2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
