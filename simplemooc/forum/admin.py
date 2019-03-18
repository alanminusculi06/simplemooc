from django.contrib import admin
from .models import Thread, Reply

class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'author__email', 'body']

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['thread', 'author', 'created_at', 'updated_at']
    search_fields = ['thread__title', 'author__email', 'message']

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply, ReplyAdmin)