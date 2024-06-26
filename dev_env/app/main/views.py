from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': "Home",
        'content': 'Главная страница магазина'
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
