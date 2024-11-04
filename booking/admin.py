from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, BookingRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds the rich-text editor for content in admin panel.
    """
    summernote_fields = ('content',)


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    """
    Lists the confirmed, booking_date, booking_time and 
    guests fields for display in admin.
    """
    list_display = ('confirmed', 'booking_date', 'booking_time', 'guests',)
