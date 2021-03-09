from django.shortcuts import render
from django.http.response import HttpResponse
import requests
import random

# 사용자가 입력할 form & input 용 **HTML 제공**
def ping(request):
    return render(request, 'practice0309/ping.html')

def pong(request):
    qd = request.GET
    # <Querydict:{'kor-name': ['나영'], 'eng-name': ['na0i']}>
    kr_name = request.GET.get('kor-name')
    en_name = request.GET.get('eng-name')
    fullname = kr_name + en_name
    context = {
        'fullname': fullname,
    }
    return render(request, 'practice0309/pong.html', context)

def var_route(request, value):
    return HttpResponse(value)

def lotto(request, no):
    # 1. 현실 로또 번호를 가져온다.
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={{ no }}'
    data = requests.get(url).json()
    
    
    real_numbers = []
    for  k, v in data.items():
        if 'drwtNo' in k:
            real_numbers.append(v)
    bnus_no = data['bnusNo']


    result = {f'{i}등': 0 for i in range(1, 6)}
    result['꽝'] = 0

    for _ in range(10000):
        my_numbers = random.sample(range(1, 46), 6)
        match_cnt = len(set(real_numbers) & set(my_numbers))
        if match_cnt == 6:
            result['1등'] += 1
        elif match_cnt == 5 and bnus_no in my_numbers:
            result['2등'] += 1
        elif match_cnt == 5:
            result['3등'] += 1
        elif match_cnt == 4:
            result['4등'] += 1
        elif match_cnt == 3:
            result['5등'] += 1
        else:
            result['꽝'] += 1    

    context = {
        'no': data['drwNo'],
        'result': result,
        'real_numbers': real_numbers,
        'bnus_no': bnus_no,
    }
    # 2. 1000번

    return render(request, 'practice0309/lotto.html', context)