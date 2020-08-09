from django.utils import timezone

from .models import GarbageDay


def update_garbage_days():
    current_date = timezone.now()
    garbage_days = GarbageDay.objects.all()

    for garbage_day in garbage_days:
        if garbage_day.next_garbage_day < current_date:
            return False
