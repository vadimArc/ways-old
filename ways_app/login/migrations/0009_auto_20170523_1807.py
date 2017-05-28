# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170519_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile_followers',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='profile_following',
            name='following',
        ),
        migrations.RemoveField(
            model_name='user_list',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user_list',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='list',
        ),
        migrations.RemoveField(
            model_name='places',
            name='list',
        ),
        migrations.AddField(
            model_name='cities',
            name='name',
            field=models.CharField(default='dao', max_length=30),
        ),
        migrations.AddField(
            model_name='places',
            name='name',
            field=models.CharField(default='dao', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='cities',
            field=models.ManyToManyField(to='login.Cities'),
        ),
        migrations.DeleteModel(
            name='Profile_followers',
        ),
        migrations.DeleteModel(
            name='Profile_following',
        ),
        migrations.DeleteModel(
            name='User_list',
        ),
        migrations.AddField(
            model_name='lists',
            name='city',
            field=models.ManyToManyField(to='login.Cities'),
        ),
        migrations.AddField(
            model_name='lists',
            name='followers',
            field=models.ManyToManyField(related_name='followers_lists', to='login.Profile'),
        ),
        migrations.AddField(
            model_name='lists',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_lists', to='login.Profile'),
        ),
        migrations.AddField(
            model_name='lists',
            name='places',
            field=models.ManyToManyField(to='login.Places'),
        ),
    ]
