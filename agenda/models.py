from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Unconfirmed"), (1, "Approved"))

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="active_events"
    )
    description = models.TextField()
    event_date = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)


class Comment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
