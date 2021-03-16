from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ContactForm, ArticleForm

def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'articles/contact.html', context)
    elif request.method == 'POST':
        contact_form = ContactForm(request.POST)
        print(contact_form.is_valid())
        print(contact_form.errors)
        return redirect('contact')

# CRUD
def new(request):
    # 사용자 요청이 get일 경우
    if request.method == 'GET':
        # 비어있는 새로운 form 생성
        form = ArticleForm()
        context = {'form': form}
        # html에 form 실어서 전송
        return render(request, 'articles/new.html', context)

    # 사용자 요청이 post인 경우
    elif request.method == 'POST':
        # form에 요청 data 입력
        form = ArticleForm(request.POST)
        # form을 통해 data 유효성 검사
        if form.is_valid():
            # 유효하면 저장
            article = form.save()
            # 저장한 article 상세보기 페이지로 redirect
            return redirect('detail', article_pk=article.pk)
        else:
            # 유효하지 않다면, 기존의 잘못된 data를 담은 form(LINE 34)을 담고
            context = {'form': form}
            # html에 실어서 전송
            return render(request, 'articles/new.html', context)

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    # 특정 article을 골라낼 수 있느냐가 우선되어야함
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        # new와 다르게, 특정 article에 대한 내용을 request.POST로 덮어쓰기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('detail', article.pk)
    elif request.method == 'GET':
        # 기존 게시글 내용을 포함한 HTML을 만들기 위해 instance 추가
        form = ArticleForm(instance=article)

    context = {'form': form}
    return render(request, 'articles/edit.html', context)

    # if request.method == 'GET':
    #     # 기존 게시글 내용을 포함한 HTML을 만들기 위해 instance 추가
    #     form = ArticleForm(instance=article)
    #     context = {'form': form}
    #     return render(request, 'articles/edit.html', context)

    # elif request.method == 'POST':
    #     # new와 다르게, 특정 article에 대한 내용을 request.POST로 덮어 쓰기
    #     form = ArticleForm(request.POST, instance=article)
    #     if form.is_valid():
    #         article = form.save()
    #         return redirect('detail', article_pk=article.pk)
    #     else:
    #         form = ArticleForm(instance=article)
    #         context = {'form': form}
    #         return render(request, 'articles/new.html', context)


def delete(request, article_pk):
    return redirect()
