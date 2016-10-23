# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 21:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BLEIdentificaiton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minor', models.IntegerField()),
                ('major', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(max_length=30)),
                ('genre', models.IntegerField(choices=[(0, b'Male'), (1, b'Female')])),
                ('birthday', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NFCIdentification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=100)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ums.Driver')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bleidentificaiton',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ums.Driver'),
        ),
    ]
