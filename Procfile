release: python manage.py migrate
web: gunicorn Roomscout.wsgi
worker: celery -A Roomscout worker -B -l INFO