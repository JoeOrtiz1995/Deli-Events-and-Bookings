from django.test import TestCase
from .forms import BookingForm

# Create your tests here.
class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        """Tests all fields"""
        form = BookingForm({
            'full_name': 'Joe', 
            'guests': '5', 
            'booking_date': '2024-12-23', 
            'booking_time': '12:30pm', 
            'message': 'Could we book?'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Tests for the full_name field"""
        form = BookingForm({
            'full_name': '', 
            'guests': '5', 
            'booking_date': '2024-12-23', 
            'booking_time': '12:30pm', 
            'message': 'Could we book?'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid, name is required")

    def test_booking_date_is_required(self):
        """Tests for the full_name field"""
        form = BookingForm({
            'full_name': 'Joe', 
            'guests': '5', 
            'booking_date': '', 
            'booking_time': '12:30pm', 
            'message': 'Could we book?'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid without a date")

    def test_booking_time_is_required(self):
        """Tests for the full_name field"""
        form = BookingForm({
            'full_name': 'Joe', 
            'guests': '5', 
            'booking_date': '2024-12-23', 
            'booking_time': '', 
            'message': 'Could we book?'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_message_is_required(self):
        """Tests for the full_name field"""
        form = BookingForm({
            'full_name': '', 
            'guests': '', 
            'booking_date': '2024-12-23', 
            'booking_time': '12:30pm', 
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is not valid")