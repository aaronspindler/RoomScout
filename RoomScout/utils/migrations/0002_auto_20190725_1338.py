# Generated by Django 2.2.3 on 2019-07-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ip',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
