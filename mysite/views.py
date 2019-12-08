from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request): #def는 definition을 의미한다.
    return render(request, 'blog/index.html', {}) //
#render는 함수로서 첫 번째 파라미터로 request를 두 번째 파라미터로는 템플릿인 blog안의 index.html을 받아들인다.

def Bongpyeong(request):
    return render(request, 'blog/Bongpyeong.html', {})

def inje(request):
    return render(request, 'blog/inje.html', {})

def jinhae(request):
    return render(request, 'blog/jinhae.html', {})

def gangreung(request):
    return render(request, 'blog/gangreung.html', {})
