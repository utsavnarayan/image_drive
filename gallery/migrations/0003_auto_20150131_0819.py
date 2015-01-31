# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_upload_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='pic',
            field=models.ImageField(upload_to=b'images/', verbose_name=b'Image'),
            preserve_default=True,
        ),
    ]
