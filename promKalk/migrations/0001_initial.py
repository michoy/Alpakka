# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promille', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
    ]
