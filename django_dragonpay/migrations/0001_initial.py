# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DragonpayPayout',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name=b'Transaction ID')),
                ('refno', models.CharField(blank=True, max_length=8, null=True)),
                ('user_id', models.CharField(blank=True, max_length=40, null=True)),
                ('user_name', models.CharField(blank=True, max_length=32, null=True)),
                ('processor_id', models.CharField(blank=True, choices=[(b'BDO', b'Banco De Oro'), (b'BPI', b'Bank of the Philippine Islands'), (b'CBC', b'Chinabank'), (b'EWB', b'East West Bank'), (b'LBP', b'Land Bank of the Philippines'), (b'MBTC', b'Metrobank'), (b'PNB', b'Philippine National Bank'), (b'RCBC', b'RCBC'), (b'SBC', b'Security Bank'), (b'UBP', b'Union Bank'), (b'UCPB', b'UCPB'), (b'PSB', b'PS Bank'), (b'CEBL', b'Cebuana Lhuilier'), (b'GCSH', b'GCash'), (b'SMRT', b'Smart Money')], max_length=8, null=True)),
                ('processor_detail', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=32, null=True)),
                ('mobile', models.CharField(blank=True, max_length=32, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=128)),
                ('currency', models.CharField(default=b'PHP', max_length=3)),
                ('status', models.CharField(choices=[(b'S', b'Success'), (b'F', b'Failed'), (b'P', b'Pending'), (b'G', b'In progress'), (b'V', b'Voided')], default=b'P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Payout',
                'verbose_name_plural': 'Payouts',
            },
        ),
        migrations.CreateModel(
            name='DragonpayPayoutUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('birthdate', models.DateField()),
                ('mobile', models.CharField(max_length=24)),
                ('address1', models.CharField(max_length=32)),
                ('address2', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=16)),
                ('state', models.CharField(max_length=16)),
                ('zip', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'Payout User',
                'verbose_name_plural': 'Payout Users',
            },
        ),
        migrations.CreateModel(
            name='DragonpayTransaction',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name=b'Transaction ID')),
                ('token', models.CharField(max_length=40)),
                ('refno', models.CharField(blank=True, max_length=8, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currency', models.CharField(choices=[(b'PHP', b'Philippine Peso'), (b'USD', b'US Dollar')], default=b'PHP', max_length=3)),
                ('description', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=40)),
                ('param1', models.CharField(blank=True, max_length=80, null=True)),
                ('param2', models.CharField(blank=True, max_length=80, null=True)),
                ('status', models.CharField(choices=[(b'S', b'Success'), (b'F', b'Failed'), (b'P', b'Pending'), (b'U', b'Unknown'), (b'R', b'Refund'), (b'K', b'Chargeback'), (b'V', b'Voided'), (b'A', b'Authorized')], default=b'P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
