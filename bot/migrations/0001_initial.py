# Generated by Django 3.1.7 on 2022-02-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('id_ogr', models.IntegerField(null=True, verbose_name='id организации')),
                ('inn', models.IntegerField(null=True, verbose_name='инн организации')),
            ],
        ),
    ]
