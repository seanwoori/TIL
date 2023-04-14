from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            'user', 
            'like_user',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            "title", 
            "user"
        )
