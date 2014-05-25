# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('where', models.CharField(help_text='Grober Ort, z.B. A5, B46, P3', max_length=50, verbose_name='Wo'),), ('direction', models.CharField(max_length=200, verbose_name='Richtung', blank=True),), ('what', models.CharField(default='JAM', max_length=10, verbose_name='Was?', choices=(('JAM', 'Stau',), ('SLOW', 'Stockender Verkehr',), ('DANGER', 'Gefahr',), ('PFULL', 'Parkplatz voll',), ('CLOSED', 'Sperrung',), ('DETOUR', 'Umleitung',), ('ROADWORKS', 'Baustelle',), ('OTHER', 'Sonstiges',),)),), ('text', models.TextField(verbose_name='Beschreibung'),), ('created', models.DateTimeField(verbose_name='Angelegt am'),), ('updated', models.DateTimeField(verbose_name='Aktualisiert am'),), ('prio', models.BooleanField(default=False, verbose_name='Eilmeldung'),)],
            bases = (models.Model,),
            options = {},
            name = 'Traffic',
        ),
    ]
