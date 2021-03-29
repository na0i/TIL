from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated():
        return redirect('community:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        # form = 'form',
        'form' : form ,
    }
    return render(request, 'accounts/signup.html', context)

#
@login_required
@require_http_methods(['GET', 'POST'])
def login(request):
    # if request.user.is_authenticated():
    #    return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save()
            auth_login(request, form.get_user())
            # auth_login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'community:index')
            # return reidrect('next_url' or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form ,
        # form = 'form' ,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:index')