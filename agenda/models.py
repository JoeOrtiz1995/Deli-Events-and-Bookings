from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Unconfirmed"), (1, "Approved"))

# Create your models here.
class Event(models.Model):
    """
    Stores an event related to :model:`auth.user`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="active_events"
    )
    description = models.TextField()
    event_date = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return f"{self.event_date} | {self.title} | Organised by {self.organiser}"


class Comment(models.Model):
    """
    Stores a user's comment, related to
    :model:`auth.user` & :model:`agenda.Event`.
    """
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.author}"
