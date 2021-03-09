from django.shortcuts import render
from django.http.response import HttpResponse
import random

def index(request):
    numbers = range(1, 46)
    lotto = random.sample(numbers, 6)
    return HttpResponse(f'Pick: {sorted(lotto)}')
