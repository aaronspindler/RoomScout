from __future__ import absolute_import, unicode_literals

from Roomscout.celery import app


@app.task()
def wait(email):
	return 1+1
