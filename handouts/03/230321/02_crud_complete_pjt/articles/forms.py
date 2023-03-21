from django.forms import ModelForm, CharField
from .models import Article

class ArticleForm(ModelForm):
    title = CharField(max_length=10)
    content = CharField()

    class Meta:
        model = Article
        fields = ['title', 'content']