import datetime
from django import forms
from gestion_taches.models import liste_taches
from django.forms import widgets


class ListeTachesForm(forms.ModelForm):
    date_creation = forms.DateField(
        widget=widgets.DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today()
    )
    
    date_cloture = forms.DateField(
        widget=widgets.DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today()
    )
    
    class Meta:
        model = liste_taches
        fields = '__all__'
