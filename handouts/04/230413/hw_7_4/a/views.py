# a- views.py

from rest_framework import status
from .models import Article

@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exceptions=True):
            serializer.validated_data
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)