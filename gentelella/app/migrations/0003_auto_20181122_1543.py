# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-22 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181122_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papertype',
            fields=[
                ('papertypeid', models.IntegerField(db_column='papertypeid', primary_key=True, serialize=False)),
                ('papertypename', models.CharField(blank=True, db_column='papertypename', max_length=255, null=True)),
            ],
            options={
                'db_table': 'papertype',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='edition',
            table='edition',
        ),
        migrations.AlterModelTable(
            name='grade',
            table='grade',
        ),
        migrations.AlterModelTable(
            name='pharse',
            table='pharse',
        ),
        migrations.AlterModelTable(
            name='subject',
            table='subject',
        ),
    ]