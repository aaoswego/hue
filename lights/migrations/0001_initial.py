# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LightButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_text', models.CharField(max_length=50)),
                ('button_url', models.CharField(max_length=500)),
            ],
        ),
    ]
