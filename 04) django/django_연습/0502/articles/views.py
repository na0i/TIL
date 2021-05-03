from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if require_method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    # 이부분 들여쓰기 중요
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    # 작성자 확인 꼭 하기
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance = article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance = article)
    else:
        return redirect('articles:index')
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)



@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

        
@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated():
        comment = get_object_or_404(Comment, pk = comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('article:detail', article_pk)