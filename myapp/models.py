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


    