from django.shortcuts import render
from django.contrib import messages
from .models import About, BookingRequest
from .forms import BookingForm

# Create your views here.
def about_us(request):
    """
    Renders the Booking Page's About Section, with the Bookings Form below.
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            user = request.user
            booking.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Booking Request Received!")

    about = About.objects.all().last()
    booking_form = BookingForm()

    return render(
        request, 
        "booking/booking.html",
        {
            "bookings": about, 
            "booking_form": booking_form,
        },
    )