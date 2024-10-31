from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by("-event_date")
    template_name = "agenda/index.html"
    paginate_by = 2