from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task(bind=True, ignore_result=False)
def wait():
	from_email = 'noreply@roomscout.ca'
	to_email = 'aaron@xnovax.net'
	subject = "RoomScout | You've been invited to join a house"
	text_content = 'You have been invited to join a house on RoomScout.ca, sign up or login now to view'
	html_content = ('<h1>Hello World</h1>')

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()