from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_invite_email(to_email, invite):
	from_email = 'noreply@roomscout.ca'
	to_email = to_email
	subject = "RoomScout | You've been invited to join a house"
	text_content = 'You have been invited to join a house on RoomScout.ca, sign up or login now to view'
	html_content = render_to_string('utils/house_invite_template.html', {'invite': invite})

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
