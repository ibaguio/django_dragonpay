# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-02 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dragonpay', '0002_transaction_status_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragonpaypayout',
            name='email',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dragonpaypayout',
            name='user_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
