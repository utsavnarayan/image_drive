# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150131_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload',
            name='pic',
            field=models.ImageField(upload_to=b'images/', verbose_name=b'Select an Image'),
            preserve_default=True,
        ),
    ]
