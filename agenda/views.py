from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by("event_date")
    template_name = "agenda/index.html"
    paginate_by = 2

def event_detail(request, slug):
    """
    Displays just one post in detail with the comments section below
    """

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug = slug)
    comments = event.comments.filter(approved=True).order_by("-created_on")

    return render(
        request,
        "agenda/event_detail.html",
        {"event": event,
        "comments": comments,        
        },
    )