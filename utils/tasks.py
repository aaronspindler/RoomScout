from celery import shared_task


@shared_task
def hello():
	sum = 0
	for i in range(100000):
		sum += i
	print(sum)
