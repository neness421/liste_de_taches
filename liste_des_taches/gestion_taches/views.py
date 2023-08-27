from django.http import HttpResponse
from django.shortcuts import render
from gestion_taches.form import ListeTachesForm
from gestion_taches.models import liste_taches
from django.shortcuts import redirect


def home(request):
    return render(request, 'gestion_taches/home.html')


def ajout(request):
    if request.method == 'POST':
        form = ListeTachesForm(request.POST)
        if form.is_valid():
            liste_taches = form.save()
            return redirect('tache_detail', liste_taches.id)
    else:
        form = ListeTachesForm()
    return render(request, 'gestion_taches/ajout.html', {'form': form})

def tache_detail(request, id):
    tache = liste_taches.objects.get(id=id)
    return render(
        request,
        'gestion_taches/tache_detail.html',
        {'tache': tache}
        )
