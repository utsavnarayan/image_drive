# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20150131_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='id',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='slug',
        ),
        migrations.AddField(
            model_name='upload',
            name='image_key',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
