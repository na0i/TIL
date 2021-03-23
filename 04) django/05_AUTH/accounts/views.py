from django.shortcuts import render
from .forms import get_user_model

def login(request):
    # login 검증 / HTML 만드는 forms.Form 을 써서 완료
    pass


def signup(request):
    if request.method = 'POST':
        form = CustomUserCreationForm(request.POST)
    # ... CustomUserCreationForm(request.POST)


def logout(request):
    # logout()