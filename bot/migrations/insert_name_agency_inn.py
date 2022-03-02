# Generated by Django 3.1.7 on 2022-02-04 16:59
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tulza.settings")
django.setup()
import pickle

with open('/Users/777/PycharmProjects/tulza/bot/list_actual_agency_sort', 'rb') as fp:
    _const_d = pickle.load(fp)
from django.db import migrations, models
from bot.models import Bb
def combine_names(apps, schema_editor):
    for dct in _const_d:
        for tro in dct:
            lo = int(dct[tro][0])
            obj = Bb(name=tro, id_ogr=lo, inn=dct[tro][1])
            print(obj)
            obj.save()
class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
