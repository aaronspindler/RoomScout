from __future__ import absolute_import, unicode_literals
from Roomscout.celery import app
from django.core.mail import EmailMultiAlternatives


@app.task()
def wait(a,b):
	return a+b