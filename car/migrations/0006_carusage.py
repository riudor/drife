# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0002_driver_alcoholemic_tax'),
        ('car', '0005_auto_20161024_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ums.Driver')),
            ],
        ),
    ]