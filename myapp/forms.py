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




class ChurnPredictionForm(forms.Form):
    TotalCharges = forms.DecimalField(label='Total Charges')
    tenure = forms.DecimalField(label='Tenure')
    Contract_Month_to_month = forms.ChoiceField(label='Contract (Month-to-Month)', choices=[(0, 'No'), (1, 'Yes')])
    InternetService_Fiber_optic = forms.ChoiceField(label='Internet Service (Fiber Optic)', choices=[(0, 'No'), (1, 'Yes')])
    PaymentMethod_Electronic_check = forms.ChoiceField(label='Payment Method (Electronic Check)', choices=[(0, 'No'), (1, 'Yes')])
    TechSupport_No = forms.ChoiceField(label='Tech Support (No)', choices=[(0, 'No'), (1, 'Yes')])
    OnlineSecurity_No = forms.ChoiceField(label='Online Security (No)', choices=[(0, 'No'), (1, 'Yes')])
    SeniorCitizen = forms.ChoiceField(label='Senior Citizen', choices=[(0, 'No'), (1, 'Yes')])
    PaperlessBilling_Yes = forms.ChoiceField(label='Paperless Billing (Yes)', choices=[(0, 'No'), (1, 'Yes')])
    StreamingTV_Yes = forms.ChoiceField(label='Streaming TV (Yes)', choices=[(0, 'No'), (1, 'Yes')])
    StreamingMovies_Yes = forms.ChoiceField(label='Streaming Movies (Yes)', choices=[(0, 'No'), (1, 'Yes')])
    Contract_Two_year = forms.ChoiceField(label='Contract (Two Year)', choices=[(0, 'No'), (1, 'Yes')])
    InternetService_DSL = forms.ChoiceField(label='Internet Service (DSL)', choices=[(0, 'No'), (1, 'Yes')])
    MultipleLines_No = forms.ChoiceField(label='Multiple Lines (No)', choices=[(0, 'No'), (1, 'Yes')])
    PaperlessBilling_No = forms.ChoiceField(label='Paperless Billing (No)', choices=[(0, 'No'), (1, 'Yes')])
    PaymentMethod_Credit_card = forms.ChoiceField(label='Payment Method (Credit Card)', choices=[(0, 'No'), (1, 'Yes')])
    TechSupport_Yes = forms.ChoiceField(label='Tech Support (Yes)', choices=[(0, 'No'), (1, 'Yes')])
    OnlineSecurity_Yes = forms.ChoiceField(label='Online Security (Yes)', choices=[(0, 'No'), (1, 'Yes')])
    PhoneService_Yes = forms.ChoiceField(label='Phone Service (Yes)', choices=[(0, 'No'), (1, 'Yes')])
    Dependents_Yes = forms.ChoiceField(label='Dependents (Yes)', choices=[(0, 'No'), (1, 'Yes')])
