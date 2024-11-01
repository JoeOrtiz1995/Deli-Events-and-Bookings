from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Event
from .forms import CommentForm

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

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 
                "Thanks for your comment! Once approved it will show, but you can still edit it if you'd like"
            )

    comment_form = CommentForm()

    return render(
        request,
        "agenda/event_detail.html",
        {
            "event": event,
            "comments": comments,
            "comment_form": comment_form,
        },
    )