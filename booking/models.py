from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

BOOKING_STATE = ((0, "Unconfirmed"), (1, "Confirmed"))

BOOKING_TIMES = (
    ("12:30pm", "12:30pm"), 
    ("1:00pm", "1:00pm"), 
    ("1:30pm", "1:30pm"), 
    ("2:00pm", "2:00pm"), 
    ("2:30pm", "2:30pm"),
    ("3:00pm", "3:00pm"), 
    ("3:30pm", "3:30pm"),
    ("4:00pm", "4:00pm"), 
    ("4:30pm", "4:30pm"),
    ("5:00pm", "5:00pm"), 
    ("5:30pm", "5:30pm"),
    ("6:00pm", "6:00pm"), 
    ("6:30pm", "6:30pm"),
    ("7:00pm", "7:00pm"), 
    ("7:30pm", "7:30pm"),
    ("8:00pm", "8:00pm"), 
    ("8:30pm", "8:30pm"),
    ("9:00pm", "9:00pm"),  
    ("9:30pm", "9:30pm"), 
)

GUESTS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    )

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="diner"
    )
    full_name = models.CharField(max_length=100)
    guests = models.IntegerField(choices=GUESTS, default=2)
    phone = PhoneNumberField(blank=True)
    booking_date = models.DateField(auto_now_add=False)
    booking_time = models.CharField(choices=BOOKING_TIMES, default="2:30pm")
    message = models.TextField(blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.IntegerField(choices=BOOKING_STATE, default=0)
    
    class Meta:
        ordering = ["-booking_date"]

    def __str__(self):
        return f"{self.confirmed} | {self.booking_date} | {self.booking_time} | Table for: {self.guests}"


    