# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_info_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='email',
            field=models.EmailField(default='default@test.com', max_length=100, unique=True),
        ),
    ]
