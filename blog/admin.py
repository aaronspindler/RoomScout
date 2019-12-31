from django.contrib import admin

from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


admin.site.register(BlogPost, BlogPostAdmin)
