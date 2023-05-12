from django.contrib import admin
from .models import Demande,Avis,Competance,Solution

# Register your models here.
admin.site.register(Demande)
admin.site.register(Avis)
admin.site.register(Competance)
admin.site.register(Solution)

