from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import BookingForm

# Create your views here.
def about_us(request):
    """
    Renders the Booking Page's About Section, with the Bookings Form below.
    """
    about = About.objects.all().last()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.client = request.user
            booking.save()
            message.add_message(
                request, messages.SUCCESS, 
                "Thanks you for making a booking with us! Feel free to amend or cancel your booking if you're unable to make it."
            )

    booking_form = BookingForm()

    return render(
        request, 
        "booking/booking.html",
        {
            "about": about, 
            "booking_form": booking_form,
        },
    )