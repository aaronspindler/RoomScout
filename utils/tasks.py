import time

from celery import shared_task


@shared_task
def wait(length):
	time.sleep(length)
