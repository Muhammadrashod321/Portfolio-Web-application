from django import forms
from article.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("article","author_full_name","author_image","comment")