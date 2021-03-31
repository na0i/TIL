from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def create_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('board:article_detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {'article_form': article_form, }
    return render(request, 'board/form.html', context)


def article_index(request):
    articles = Article.objects.order_by('-updated_at')
    context = {'articles': articles, }
    return render(request, 'board/article_index.html', context)


def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'board/article_detail.html', context)


def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('board:article_detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {'article_form': article_form, }
    return render(request, 'board/form.html', context)


def delete_article(request, article_pk):
    pass


def create_comment(request, article_pk):    
    # 1. article 찾지 않고
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('board:article_detail', article.pk)  # 1. 2번인자 article_pk로 redirect 하기
    else:
        return redirect('board:article_detail', article.pk)


def update_comment(request, article_pk, comment_pk):
    pass


def delete_comment(request, article_pk, comment_pk):
    pass






