# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(blank=True, null=True, max_length=60)),
                ('start_date', models.DateTimeField(blank=True, null=True, help_text='When do you want to start this workshop.')),
                ('end_date', models.DateTimeField(blank=True, null=True, help_text='This is optional')),
                ('duree', models.PositiveIntegerField(blank=True, null=True, help_text='How many minutes or hours that this workshop will last.', default=45)),
                ('measuring_unit', models.CharField(choices=[('hr', 'hour'), ('hrs', 'hours'), ('min', 'minutes')], default='minutes', max_length=8)),
                ('language', models.CharField(choices=[('FR', 'Francais'), ('EN', 'English')], default='En', max_length=2)),
                ('event_type', models.CharField(choices=[('workshop', 'Workshop'), ('atelier', 'Atelier'), ('course', 'Course'), ('cours', 'Cours')], default='workshop', max_length=10)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('description', models.TextField(blank=True, null=True, help_text='Please write about what user will benefit from subscribing to this Event.')),
                ('photo', models.ImageField(upload_to='events/%Y/%m/%d', blank=True, null=True)),
                ('slug', models.CharField(max_length=200)),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(verbose_name='标签', help_text='Enter the Comma separated Taxonomy', through='taggit.TaggedItem', blank=True, to='taggit.Tag')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'activities',
                'verbose_name_plural': 'activities',
            },
        ),
    ]
