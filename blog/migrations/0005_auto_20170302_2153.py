# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
