from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ingests bitcoin data'

    def handle(self, *args, **options):
        pass