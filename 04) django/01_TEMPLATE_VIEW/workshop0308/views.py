from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    lotto = random.sample(range(1, 46), 6)
    # 딕셔너리 형태여야 함, 이름을 불러야하기 때문에
    context = {
        'lotto': sorted(lotto),
        'greeting': 'Hello world!'
    }
    return render(request, 'workshop0308/lotto.html', context)