from django import forms
from .models import Article, Comment
from django.http import HttpRequest
from django.contrib.auth.middleware import AuthenticationMiddleware


class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    # 1. validation, 2. HTML
    content = forms.CharField(max_length=300)
    class Meta:
        model = Comment
        fields = ('content', )
        