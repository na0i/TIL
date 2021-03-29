from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


def index(request):
    reviews = Review.objects.all()
    context = {
        # '변수명' : 값
         'reviews' : reviews,
        # reviews = 'reviews',
    }
    return render(request, 'community/index.html', context)

# 로그인한 사람만
@login_required
#
@require_http_methods(['GET', 'POST'])
def create(request):
    # if request.user.is_authenticated():
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form,
        # form = 'form'
    }
    return render(request, 'community/form.html', context)

# decorator
@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # review의 comment를 가져오는 것이므로
    comment = review.comment.set_all()
    # comments = Review.comment.set_all()
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comments' : comments,
        'comment_form' : commet_form,
        # review = 'review',
        # comments = 'comments',
        # comment_form = 'commet_form',
    }
    return render(request, 'community/detail.html', context)


# @login_required
# def comment(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment_form.save(commit=False)
#             comment.review = review
#             comment_form.save()
#             return redirect('community:detail')
#     else:
#         comment_form = CommentForm()

@require_POST
def comments(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk = review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
            return redirect('community:detail', review.pk)
        context = {
            'review' : review,
            'comments' : comments,
            'comment_form' : comment_form,
        }
        return render(request, 'community/detail.html', context)
    return redirect('accounts:login')


    

    