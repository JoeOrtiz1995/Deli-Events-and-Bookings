from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Comment


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    """
    Lists the display, search and filters fields,
    as well as the fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'event_date', 'status')
    search_fields = ['title', 'event_date']
    list_filter = ('title', 'event_date',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'excerpt',)


# Register your models here.
admin.site.register(Comment)
