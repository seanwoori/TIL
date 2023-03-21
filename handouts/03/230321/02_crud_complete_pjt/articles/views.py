from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save() # 아티클 저장
            return redirect('articles:detail', pk=article.pk)
        return redirect('articles:create')
    
    else:
        form = ArticleForm()
        context = {
            'form' : form
        }
        return render(request, 'articles/create.html', context)
    
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.save()
    #     return redirect('articles:detail', pk=article.pk)
    # else:
    #     return render(request, 'articles/create.html')

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article:detial', article.pk)
    else:
        form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article
            }
        return render(request, 'articles/update.html', context)
