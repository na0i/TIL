from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

def signup(request):
    #  login 한 사용자라면,
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserCreationForm()
    context = {'form': form, }
    
    return render(request, 'accounts/signup.html', context)


def login(request):
    # login 검증 / HTML 만드는 forms.Form 을 써서 완료
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인을 시켜야 하는데..
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')
            return redirect(next_url or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


# /accounts/profile/<neo>/
def profile(request, username):  # 프로필 페이지
    user = get_object_or_404(User, username=username)
    
    context = {'user_profile': user, }
    """
    request.user => /profile/<username>/ 으로 요청을 보낸 사람
    user => /profile/<username>/ 에서 username 에 해당하는 사람
    둘이 같을 때, Update 로직(form, valid 등..)이 실행됨 / 그게 아니라면 단순 조회 페이지
    """
    if request.user == user:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save()
                return redirect('accounts:profile', username=user.username)
        else:
            form = CustomUserChangeForm(instance=user)

        context['form'] = form
    
    return render(request, 'accounts/profile.html', context)


@login_required
def change_password(request):  # 비밀번호 변경
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile', form.user.username)
    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form': form, }
    return render(request, 'accounts/change_password.html', context)


@login_required
@require_POST
def withdraw(request):  # 탈퇴
    request.user.delete()  # 팔찌를 차고 있는 사람을 죽인(?!)다
    auth_logout(request)  # cookie(팔찌) 회수 + session 테이블에서 레코드 삭제
    return redirect('articles:index')


@login_required
def force_logout(request):
    from importlib import import_module
    from django.contrib.sessions.models import Session
    from django.conf import settings
    session_engine = import_module(settings.SESSION_ENGINE)
    # 유효기간 지난 SESSION DATA 모두 삭제(최적화)
    session_engine.SessionStore.clear_expired()
    sessions = Session.objects.all()
    # 모든 Session 에 대해 순회하며 해석 => 비교 후 삭제
    for session in sessions:
        data = session.get_decoded()
        if data.get('_auth_user_id'):
            user_id = int(data.get('_auth_user_id'))
        if request.user.id == user_id:
            session.delete()
    return redirect('articles:index')
        