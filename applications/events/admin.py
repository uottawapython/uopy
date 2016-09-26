from django.contrib import admin

from .models import Event
from django.utils.text import Truncator

class EventAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'start_date', 'end_date', 'status',
                    'event_type', 'description_truncated', 'photo')
    list_filter = ('status', 'created', 'modified', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author',)
    date_hierarchy = 'start_date'
    ordering = ['status']

    def description_truncated(self, obj):
        return Truncator(obj.description).chars(75)
    description_truncated.admin_order_field = 'Description'
    description_truncated.short_description = 'Description'

admin.site.register(Event, EventAdmin)
