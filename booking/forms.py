from .models import BookingRequest
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ('full_name', 'guests', 'booking_date', 'booking_time', 'message',)