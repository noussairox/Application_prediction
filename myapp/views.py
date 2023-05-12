from django.shortcuts import render ,redirect
from .forms import DemandeForm,AvisForm ,PredictionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth.views import PasswordResetConfirmView
from .models import Competance,Avis
from .utils import predict

# Create your views here.
def  index(request):
    return render(request,"index.html")

def about(request):
    context = {'com':Competance.objects.all()}
    return render(request,"about.html",context)

def service(request):
    if request.method == "POST":
        form = DemandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form =DemandeForm()
    return render(request,"service.html",{'form': form})


def solution(request):
    return render(request, "solution.html")

def avis(request):
    context = {'avis':Avis.objects.all()}
    return render(request,"avis.html",context)

def ecrireavis(request):
    if request.method == "POST":
        form = AvisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("myapp:avis")
    else:
        form = AvisForm()
    return render(request, "ecrireavis.html",{'form':form})


def contact(request):
    return render(request,"contact.html")

def voiture(request):
    return render(request,"graph/voiture.html")

def telecommunication(request):
    return render(request,"graph/telecommunication.html")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('myapp:index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {"form": form})

def prediction_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            predictions = predict(data)  # Transmettre le dictionnaire des données
            print(predictions)
            return render(request, 'result.html', {'predictions': predictions})
    else:
        form = PredictionForm()

    return render(request, 'pred/predict.html', {'form': form})
