# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'services_images', blank=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('description', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
