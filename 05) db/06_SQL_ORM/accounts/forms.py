""" 통상적인 ModelForm 생성
from django import forms

# 생성, 수정
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
"""

# User 생성/수정은, *비밀번호* 때문에 생성과 수정이 나눠졌다.
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

# 생성담당: UserCreationForm <=> auth.User(default User) <=> 수정담당: UserChangeForm 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )
