# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-19 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.common
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0004_auto_20170411_0504'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('ad_sloggan', models.CharField(help_text='The Sloggan to display under the link title', max_length=200)),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image')),
                ('ad_type', models.CharField(choices=[('BANNER', 'BANNER'), ('BRAND', 'BRAND')], default=main.common.AdType('BRAND'), max_length=255)),
                ('brand_logo', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Brand Logo')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='DisplayedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, verbose_name='URL')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('product_price', models.IntegerField(default=0, verbose_name='Product price')),
                ('discount_price', models.IntegerField(default=0, verbose_name='Discount price')),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='Product Image')),
                ('link', models.URLField(verbose_name='Product Link')),
            ],
            options={
                'verbose_name': 'Displayed Product',
                'verbose_name_plural': 'Displayed Products',
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('feature_heading', models.CharField(default='Contest Features', max_length=200)),
                ('current_contest_description', models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n        Mihi vero, inquit, placet agi subtilius et, ut ipse dixisti, pressius.', max_length=200)),
                ('recent_contest_description', models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n        Mihi vero, inquit, placet agi subtilius et, ut ipse dixisti, pressius.', help_text='This a short description of the recent contest section displayed on the home page.', max_length=200)),
            ],
            options={
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('shop_name', models.CharField(default='Shop 1', max_length=1000, verbose_name='Shop Name')),
                ('shop_description', models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n        Mihi vero, inquit, placet agi subtilius et, ut ipse dixisti, pressius.', help_text='This a short description of the shopping section displayed on the home page.', max_length=200)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping', to='main.HomePage')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Shopping Area',
                'verbose_name_plural': 'Shopping Area',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('media_type', models.CharField(choices=[('FACEBOOK', 'FACEBOOK'), ('INSTAGRAM', 'INSTAGRAM'), ('YOUTUBE', 'YOUTUBE'), ('LINKEDIN', 'LINKEDIN'), ('PINTEREST', 'PINTEREST'), ('TWITTER', 'TWITTER'), ('WHATSAPP', 'WHATSAPP')], default=main.common.SocialMediaType('FACEBOOK'), max_length=255)),
                ('link', models.CharField(blank=True, help_text='Optional, if provided clicking the blurb will go here.', max_length=2000)),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='displayedproduct',
            name='shopping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.Shopping'),
        ),
        migrations.AddField(
            model_name='displayedproduct',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='adslider',
            name='homepage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adslides', to='main.HomePage'),
        ),
        migrations.AddField(
            model_name='adslider',
            name='link',
            field=models.ForeignKey(help_text='Clicking the Slider will go here.', on_delete=django.db.models.deletion.CASCADE, to='pages.Link'),
        ),
    ]
