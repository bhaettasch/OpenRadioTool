# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20140603_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherforecast',
            name='end',
        ),
    ]
