from django.urls import path

from .views import home_page, candles_page, soap_page, cups_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('candles/', candles_page, name='candles'),
    path('soap/', soap_page, name='soap'),
    path('cups/', cups_page, name='cups')
]
