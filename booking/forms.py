from django import forms
from .models import BookingRequest


class BookingForm(forms.ModelForm):
    """
    Form class for Users to submit booking requests.
    """
    class Meta:
        """
        Indicates the model used and the order in which to display the fields.
        """
        model = BookingRequest
        fields = ('full_name', 'guests', 'booking_date', 'booking_time', 'message',)