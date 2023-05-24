from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Demande(models.Model):
    nom_complet = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=[('webdev', 'Développement Web'), ('ml', 'Machine Learning'), ('dl', 'Deep Learning'), ('consultation', 'Consultation'), ('mobiledev', 'Développement Mobile')])
    objet = models.CharField(max_length=100) 
    message = models.TextField()
    creation_demande = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nom_complet
    
class Avis(models.Model):
    nom = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    avis = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')

    def __str__(self):
        return self.nom
    
class Competance(models.Model):
    nom = models.CharField(max_length=100)
    pourcentage = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Solution(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_ajout = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return self.link
    
    
class Article(models.Model):
    x =[
        ('General','General'),
        ('Developement','Developement'),
        ('Ai','Ai')
    ]
    titre = models.CharField(max_length=255)
    subtitre = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    category = models.CharField(max_length=255,null=True,blank=True,choices=x)
    slug = models.SlugField(unique=True,null=True,blank=True)
    date_creation = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subtitre
    
    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})


class Prediction(models.Model):
    Marque = models.CharField(max_length=255)
    Modele = models.CharField(max_length=255)
    Annee_Modele = models.IntegerField(blank=True, null=True)
    Type_de_carburant = models.CharField(max_length=255)
    Puissance_fiscale = models.IntegerField(blank=True, null=True)
    Kilometrage = models.CharField(max_length=255)
    etat = models.CharField(max_length=255)
    Boite_de_vitesses = models.CharField(max_length=255)
    Nombre_de_portes = models.IntegerField(blank=True, null=True)
    Origine = models.CharField(max_length=255)
    Premiere_main = models.CharField(max_length=255)
    Jantes_aluminium = models.BooleanField(blank=True,null=True)
    Airbags = models.BooleanField(blank=True,null=True)
    Climatisation = models.BooleanField(blank=True,null=True)
    Systeme_de_navigation_GPS = models.BooleanField(blank=True,null=True)
    Toit_ouvrant = models.BooleanField(blank=True,null=True)
    Sieges_cuir = models.BooleanField(blank=True,null=True)
    Radar_de_recul = models.BooleanField(blank=True,null=True)
    Camera_de_recul = models.BooleanField(blank=True,null=True)
    Vitres_electriques = models.BooleanField(blank=True,null=True)
    ABS = models.BooleanField(blank=True,null=True)
    ESP = models.BooleanField(blank=True,null=True)
    Regulateur_de_vitesse = models.BooleanField(blank=True,null=True)
    Limiteur_de_vitesse = models.BooleanField(blank=True,null=True)
    CD_MP3_Bluetooth = models.BooleanField(blank=True,null=True)
    Ordinateur_de_bord = models.BooleanField(blank=True,null=True)
    Verrouillage_centralise_a_distance = models.BooleanField(blank=True,null=True)
    price_model1 = models.FloatField()
    price_model2 = models.FloatField()
    price_model3 = models.FloatField()

    def __str__(self):
        return f"Prédiction : {self.Marque}, {self.Modele}, {self.price_model2} MAD"
    

class PredictionChurn(models.Model):
    TotalCharges = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.DecimalField(max_digits=10, decimal_places=2)
    Contract_Month_to_month = models.BooleanField()
    InternetService_Fiber_optic = models.BooleanField()
    PaymentMethod_Electronic_check = models.BooleanField()
    TechSupport_No = models.BooleanField()
    OnlineSecurity_No = models.BooleanField()
    SeniorCitizen = models.BooleanField()
    PaperlessBilling_Yes = models.BooleanField()
    StreamingTV_Yes = models.BooleanField()
    StreamingMovies_Yes = models.BooleanField()
    Contract_Two_year = models.BooleanField()
    InternetService_DSL = models.BooleanField()
    MultipleLines_No = models.BooleanField()
    PaperlessBilling_No = models.BooleanField()
    PaymentMethod_Credit_card = models.BooleanField()
    TechSupport_Yes = models.BooleanField()
    OnlineSecurity_Yes = models.BooleanField()
    PhoneService_Yes = models.BooleanField()
    Dependents_Yes = models.BooleanField()
    prediction_lr = models.CharField(max_length=20)
    prediction_rf = models.CharField(max_length=20)
    prediction_svm = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id}"