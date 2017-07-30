# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 18:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0003_auto_20170730_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sites_created', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='editors',
            field=models.ManyToManyField(related_name='sites_that_can_be_edited', to=settings.AUTH_USER_MODEL),
        ),
    ]