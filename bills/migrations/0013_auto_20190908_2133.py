# Generated by Django 2.2.4 on 2019-09-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0012_remove_bill_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='type',
            field=models.CharField(choices=[('ELEC', 'Electricity'), ('WATER', 'Water'), ('GAS', 'Gas'), ('INTER', 'Internet'), ('OTHER', 'Other')], max_length=5),
        ),
    ]