from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'scheduled_time', 'image')  # Use actual field names


admin.site.register(Post, PostAdmin)
