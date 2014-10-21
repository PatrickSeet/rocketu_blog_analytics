# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141018_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ad_url', models.URLField(unique=True)),
                ('ad_name', models.CharField(max_length=50)),
                ('ad_image', models.ImageField(upload_to=b'ad_image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
