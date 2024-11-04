from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import About, BookingRequest
from .forms import BookingForm

# Create your views here.
def about_us(request):
    """
    Renders the Booking Page's About Section, with the Bookings Form below.
    """

    about = About.objects.all().last()
    bookings = BookingRequest.objects.filter()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.client = request.user
            booking.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Booking Request Received!")
        else:
            messages.add_message(request, messages.ERROR, "Sorry, it's not been possible to submit your booking request, plese try again or contact us.")

    booking_form = BookingForm()

    return render(
        request, 
        "booking/booking.html",
        {
            "about": about, 
            "bookings": bookings, 
            "booking_form": booking_form,
        },
    )
