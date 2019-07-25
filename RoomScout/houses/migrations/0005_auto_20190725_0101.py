# Generated by Django 2.2.3 on 2019-07-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_house_hide_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='address',
        ),
        migrations.AddField(
            model_name='house',
            name='street_name',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='house',
            name='street_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='house',
            name='prov_state',
            field=models.CharField(max_length=2),
        ),
    ]
