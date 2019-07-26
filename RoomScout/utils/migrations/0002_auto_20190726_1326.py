# Generated by Django 2.2.3 on 2019-07-26 17:26

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import RoomScout.storage_backends


class Migration(migrations.Migration):
	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
		('utils', '0001_initial'),
	]

	operations = [
		migrations.AddField(
			model_name='privatefile',
			name='is_approved',
			field=models.BooleanField(default=False),
		),
		migrations.AddField(
			model_name='privatefile',
			name='uploaded_at',
			field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
			preserve_default=False,
		),
		migrations.CreateModel(
			name='PrivateImage',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('uploaded_at', models.DateTimeField(auto_now_add=True)),
				('is_approved', models.BooleanField(default=False)),
				('image', models.ImageField(storage=RoomScout.storage_backends.PrivateMediaStorage(), upload_to='')),
				('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
			],
		),
	]
