from django.shortcuts import render
from .models import About

# Create your views here.
def about_us(request):
    """
    Renders the Booking Page's About Section
    """
    about = About.objects.all().last()

    return render(
        request, 
        "booking/booking.html",
        {
            "about": about
        },
    )