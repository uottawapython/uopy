# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160605_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True, help_text='Please write about what user will benefit from subscribing to this Event.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='duree',
            field=models.PositiveIntegerField(default=45, null=True, verbose_name='Duree', blank=True, help_text='How many minutes or hours that this workshop will last.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='End_date', blank=True, help_text='This is optional'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(default='workshop', choices=[('workshop', 'Workshop'), ('atelier', 'Atelier'), ('course', 'Course'), ('cours', 'Cours')], max_length=10, verbose_name='Event_type'),
        ),
        migrations.AlterField(
            model_name='event',
            name='language',
            field=models.CharField(default='En', choices=[('FR', 'Francais'), ('EN', 'English')], max_length=2, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='event',
            name='measuring_unit',
            field=models.CharField(default='minutes', choices=[('hr', 'hour'), ('hrs', 'hours'), ('min', 'minutes')], max_length=8, verbose_name='Measuring_unit'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, verbose_name='Photo', blank=True, upload_to='events/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.CharField(max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='Start_date', blank=True, help_text='When do you want to start this workshop.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default='draft', choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(null=True, max_length=60, verbose_name='Title', blank=True),
        ),
    ]
