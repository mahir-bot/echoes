from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('This is Home Page')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about mahir')
    return render(request, 'about.html')
