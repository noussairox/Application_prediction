from django import forms
from .models import Demande,Avis
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ('nom_complet','email','telephone','service','objet','message')

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ('nom','service','avis','image')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class PredictionForm(forms.Form):
    Marque = forms.CharField()
    Modele = forms.CharField()
    Annee_Modele = forms.IntegerField()
    Type_de_carburant = forms.CharField()
    Puissance_fiscale = forms.IntegerField()
    Kilometrage = forms.CharField()
    etat = forms.CharField()
    Boite_de_vitesses = forms.CharField()
    Nombre_de_portes = forms.IntegerField()
    Origine = forms.CharField()
    Premiere_main = forms.CharField()
    Jantes_aluminium = forms.BooleanField(required=False, initial=True)
    Airbags = forms.BooleanField(required=False, initial=False)
    Climatisation = forms.BooleanField(required=False, initial=False)
    Systeme_de_navigation_GPS = forms.BooleanField(required=False, initial=False)
    Toit_ouvrant = forms.BooleanField(required=False, initial=False)
    Sieges_cuir = forms.BooleanField(required=False, initial=False)
    Radar_de_recul = forms.BooleanField(required=False, initial=False)
    Camera_de_recul = forms.BooleanField(required=False, initial=False)
    Vitres_electriques = forms.BooleanField(required=False, initial=False)
    ABS = forms.BooleanField(required=False, initial=False)
    ESP = forms.BooleanField(required=False, initial=False)
    Regulateur_de_vitesse = forms.BooleanField(required=False, initial=False)
    Limiteur_de_vitesse = forms.BooleanField(required=False, initial=False)
    CD_MP3_Bluetooth = forms.BooleanField(required=False, initial=False)
    Ordinateur_de_bord = forms.BooleanField(required=False, initial=False)
    Verrouillage_centralise_a_distance = forms.BooleanField(required=False, initial=False)
