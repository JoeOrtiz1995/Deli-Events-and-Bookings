from django.test import TestCase
from .forms import CommentForm

# Create your tests here.
class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'author': 'DOrtiz'})
        self.assertTrue(comment_form.is_valid())