from django.contrib import admin
from .models import Thread, Reply, Profile

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'total_likes', 'total_dislikes')
    list_filter = ('date_created',)
    search_fields = ('title', 'description')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('thread', 'user', 'date_created', 'message')
    list_filter = ('date_created', 'user')
    search_fields = ('message', 'user__username', 'thread__title')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply, ReplyAdmin)