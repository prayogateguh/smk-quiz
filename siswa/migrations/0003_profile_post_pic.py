# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0002_profile_sudah_ujian'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
