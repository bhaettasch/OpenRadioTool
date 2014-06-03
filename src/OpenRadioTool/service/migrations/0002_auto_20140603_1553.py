# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weather', models.CharField(max_length=200, verbose_name=b'Wetter')),
                ('minTemperature', models.FloatField(verbose_name=b'Minimale Temperatur')),
                ('maxTemperature', models.FloatField(verbose_name=b'Maximale Temperatur')),
                ('humidity', models.FloatField(verbose_name=b'Feuchtigkeit')),
                ('symbol', models.CharField(max_length=3)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
            options={
                'ordering': [b'begin'],
                'verbose_name': b'Wettervorhersage',
                'verbose_name_plural': b'Wettervorhersagen',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='updated',
            field=models.DateTimeField(verbose_name=b'Aktualisiert am', editable=False),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='created',
            field=models.DateTimeField(verbose_name=b'Angelegt am', editable=False),
        ),
        migrations.AlterField(
            model_name='traffic',
            name='prio',
            field=models.BooleanField(default=False, help_text=b'Besonders wichtige und dringende Meldung', verbose_name=b'Eilmeldung'),
        ),
    ]
