# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20140603_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCurrent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weather', models.CharField(max_length=200, verbose_name=b'Wetter')),
                ('temperature', models.FloatField(verbose_name=b'Aktuelle Temperatur')),
                ('humidity', models.FloatField(help_text=b'%', verbose_name=b'Feuchtigkeit')),
                ('symbol', models.CharField(max_length=3)),
                ('updated', models.DateTimeField(verbose_name=b'Letzte Aktualisierung', editable=False)),
            ],
            options={
                'verbose_name': b'Aktuelles Wetter',
                'verbose_name_plural': b'Aktuelles Wetter',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='weatherforecast',
            name='humidity',
            field=models.FloatField(help_text=b'%', verbose_name=b'Feuchtigkeit'),
        ),
    ]
