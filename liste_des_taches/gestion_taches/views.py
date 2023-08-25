from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'gestion_taches/home.html')
