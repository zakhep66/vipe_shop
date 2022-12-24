from django.shortcuts import render


def home_page(request):
    return render(request, 'web_site/home_page.html', {'title': 'Главная страница'})
