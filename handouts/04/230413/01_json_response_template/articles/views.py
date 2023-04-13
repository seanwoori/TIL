from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.core import serializers


# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    article_json = []

    for article in articles:
        article_json.append(
            {
        'id' : article.pk,
        'title' : article.title,
        'content' : article.content,
        'created_at' : article.create_at,
        'updated_at' : article.update_at,
            }
        )

    return JsonResponse(article_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)