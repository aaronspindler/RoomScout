import datetime

def now():
	return datetime.datetime.now()

def time_diff_display(updated):
	now = datetime.datetime.now(datetime.timezone.utc)
	updated = updated
	diff = now - updated
	diff_seconds = diff.total_seconds()
	diff_minutes = divmod(diff_seconds, 60)[0]
	diff_hours = divmod(diff_seconds, 3600)[0]
	diff_days = divmod(diff_seconds, 86400)[0]

	if (diff_hours < 1):
		return ('Less than 1 hour ago')
	elif (diff_hours == 1):
		return ('1 hour ago')
	elif (diff_hours < 24 and diff_hours >= 1):
		return (str(int(diff_hours)) + ' hours ago')
	elif (diff_hours < 24):
		return ('Less than 1 day ago')
	elif (diff_days == 1):
		return ('1 day ago')
	else:
		return (str(int(diff_days)) + ' days ago')
