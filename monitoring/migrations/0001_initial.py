# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBFFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(upload_to=b'')),
                ('file2', models.FileField(upload_to=b'')),
            ],
        ),
    ]
