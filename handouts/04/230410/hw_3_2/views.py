# views.py
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    comment_form = CommentForm()
    context_data = {
        'article': article,
        'comments': comment_form,
    }
    return render(request, 'eithers/detail.html', context_data)