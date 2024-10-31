from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'event_date')
    search_fields = ['title', 'event_date']
    list_filter = ('title', 'event_date',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'excerpt',)    

# Register your models here.
admin.site.register(Comment)