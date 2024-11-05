from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Comment
from .forms import CommentForm


# Create your views here.
class EventList(generic.ListView):
    """
    Renders all the approved Events in :model:`agenda.Event`
    and displays these as 2 rows of 2 events.
    **Context**
    ``queryset``
        All instances of :model:`agenda.Event`.
    ``paginate_by``
        States how many events to display.
    **Template**
    :template:`agenda/index.html`
    """
    queryset = Event.objects.filter(status=1).order_by("event_date")
    template_name = "agenda/index.html"
    paginate_by = 4


def event_detail(request, slug):
    """
    Displays just one post in detail with the comments section below.
    :model:`event.Comment`
    **Context**
    ``event``
        A specific instance of :model:`agenda.Event`.
    ``comments``
        All comments related to the event and authorised.
    ``comment_form``
        An instance of :form:`agenda.CommentForm`
    **Template**
    :template:`agenda/event_detail.html`
    """
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comments = event.comments.all().order_by("-created_on")

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


def edit_comment(request, slug, comment_id):
    """
    View for Users to edit comments
    **Context**
    ``event``
        A specific instance of :model:`agenda.Event`.
    ``comment``
        A single comment related to the event and authorised.
    ``comment_form``
        An instance of :form:`agenda.CommentForm`
    """
    if request.method == "POST":

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, there's been an Error updating your comment")

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))


def delete_comment(request, slug, comment_id):
    """
    View for Users to delete comments
    **Context**
   ``event``
        A specific instance of :model:`agenda.Event`.
    ``comment``
        A single comment related to the event and authorised.
    ``comment_form``
        An instance of :form:`agenda.CommentForm`
    """
    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Your comment has been deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            "It's only possible to delete your own comments")

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))
