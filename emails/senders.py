from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import EmailMessage


# TODO Put this into a celery background task
def send_invite_email(to_email, invite):
	from_email = 'noreply@roomscout.ca'
	to_email = to_email
	subject = "RoomScout | You've been invited to join a house"
	text_content = 'You have been invited to join a house on RoomScout.ca, sign up or login now to view'
	html_content = render_to_string('utils/house_invite_template.html', {'invite': invite})

	database_msg = EmailMessage()
	database_msg.from_email = from_email
	database_msg.to_email = to_email
	database_msg.subject = subject
	database_msg.text_content = text_content
	database_msg.html_content = html_content
	database_msg.save()

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()


# TODO Put this into a celery background task
def send_inquiry_email(to_email, inquiry):
	from_email = 'noreply@roomscout.ca'
	to_email = to_email
	subject = "RoomScout | Someone is interested in your room"
	text_content = 'Someone is interested in ' + inquiry.room.name + ' at ' + inquiry.room.house.full_address()
	html_content = render_to_string('utils/room_inquiry_template.html', {'inquiry': inquiry})

	database_msg = EmailMessage()
	database_msg.from_email = from_email
	database_msg.to_email = to_email
	database_msg.subject = subject
	database_msg.text_content = text_content
	database_msg.html_content = html_content
	database_msg.save()

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()


# TODO Put this into a celery background task
def send_contact_us_email(submitter_email, submitter_subject, submitter_message, ip):
	from_email = 'noreply@roomscout.ca'
	# TODO : make this send to all staff members emails
	to_email = 'aaron@xnovax.net'
	subject = "RoomScout | Someone has tried to contact us!"
	text_content = 'Someone has tried to contact us'
	html_content = render_to_string('utils/contact_us_template.html', {'email': submitter_email, 'subject': submitter_subject, 'message': submitter_message, 'ip': ip})

	database_msg = EmailMessage()
	database_msg.from_email = from_email
	database_msg.to_email = to_email
	database_msg.subject = subject
	database_msg.text_content = text_content
	database_msg.html_content = html_content
	database_msg.save()

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()


# TODO Put this into a celery background task
def send_bill_email(house, bill):
	from_email = 'noreply@roomscout.ca'
	to_emails = []
	for member in house.members.all():
		if member.general_contact:
			to_emails.append(member.email)

	if len(to_emails) > 0:
		subject = "RoomScout | New Bill"
		# TODO: Add a way to randomize email with funny text
		text_content = 'Your landlord has added a new bill to your house!'
		# TODO: Improve template to include more details
		html_content = render_to_string('utils/bill_added_template.html', {'bill': bill, 'house': house})

		for email in to_emails:
			database_msg = EmailMessage()
			database_msg.from_email = from_email
			database_msg.to_email = email
			database_msg.subject = subject
			database_msg.text_content = text_content
			database_msg.html_content = html_content
			database_msg.save()

		msg = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
		msg.attach_alternative(html_content, "text/html")
		msg.send()
