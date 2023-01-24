from django.shortcuts import render
from .models import Candles, Cups, Soap


def home_page(request):
    return render(request, 'web_site/home_page.html', {'title': 'Главная страница'})


def candles_page(request):
    candles = Candles.objects.all()
    context = {'context': candles}
    return render(request, 'web_site/candles_page.html', context)


def cups_page(request):
    cups = Cups.objects.all()
    context = {'context': cups}
    return render(request, 'web_site/cups_page.html', context)


def soap_page(request):
    soap = Soap.objects.all()
    context = {'context': soap}
    return render(request, 'web_site/soap_page.html', context)
