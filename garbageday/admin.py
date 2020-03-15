from django.contrib import admin

from .models import GarbageDay


class GarbageDayAdmin(admin.ModelAdmin):
    list_display = ('house', 'user', 'last_garbage_day', 'next_garbage_day', 'garbage_frequency')


admin.site.register(GarbageDay, GarbageDayAdmin)
