from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for Users to comment.
    """
    class Meta:
        """
        Indicates the model used and field order.
        """
        model = Comment
        fields = ('body',)