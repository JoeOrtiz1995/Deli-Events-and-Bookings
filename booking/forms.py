from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('full_name', 'guests', 'phone', 'booking_date', 'booking_time', 'message',)