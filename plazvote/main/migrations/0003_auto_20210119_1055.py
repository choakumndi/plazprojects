# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-19 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210119_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adslider',
            options={'ordering': ('_order',), 'verbose_name': 'Advert', 'verbose_name_plural': 'Adverts'},
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='_meta_title',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='created',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='description',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='gen_description',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='in_sitemap',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='keywords_string',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='short_url',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='site',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='status',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='title',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='updated',
        ),
    ]
