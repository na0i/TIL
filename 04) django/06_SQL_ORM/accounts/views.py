from django.shortcuts import render, redirect   
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# User table Create
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_login(request, new_user)
            return redirect('accounts:profile')
    else:
        form = CustomUserCreationForm()        
    context = {'form': form, }

    return render(request, 'accounts/signup.html', context)


# User table detail
@login_required
def profile(request):
    # 기존에는 아래와 같이 특정 객체를 불러오지만, 요청을 보낸 사용자는 request.user 로 바로 가져올 수 있음
    # article = get_object_or_404(Article, pk=article_pk)
    me = request.user
    context = {'me': me, }
    return render(request, 'accounts/profile.html', context)

###########################################

# Session table Create => AuthenticationForm 은 save 없음!
def login(request):
    if request.method == 'POST':
        # AuthForm 은 사용자가 제출한 id/pw가 올바른(User DB에 있는)지 검증함.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():  # 검증이 올바르게 끝나면, id/pw 에 매칭하는 사용자 추출 가능
            old_user = form.get_user()
            # form.save() X => auth_login() O
            auth_login(request, old_user)  # Session 테이블에 추가 + 팔찌
            return redirect('accounts:profile')
    else:
        form = AuthenticationForm(request)
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)
    

# Session table Delete
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')