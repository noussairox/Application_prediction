from django.shortcuts import render ,redirect,get_object_or_404
from .forms import DemandeForm,AvisForm ,PredictionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm,ChurnPredictionForm
from django.urls import reverse
from django.contrib.auth.views import PasswordResetConfirmView
from .models import Competance,Avis,Article
from .utils import predict,make_churn_prediction
from django.views.generic import DetailView
from django.db.models import Count


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
            return render(request, 'pred/result.html', {'predictions': predictions})
    else:
        form = PredictionForm()

    return render(request, 'pred/predict.html', {'form': form})


def churn_prediction_view(request):
    if request.method == 'POST':
        form = ChurnPredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Préparer les données d'entrée pour la prédiction
            input_values = [
                data['TotalCharges'],
                data['Contract_Month_to_month'],
                data['InternetService_Fiber_optic'],
                data['PaymentMethod_Electronic_check'],
                data['TechSupport_No'],
                data['OnlineSecurity_No'],
                data['SeniorCitizen'],
                data['PaperlessBilling_Yes'],
                data['StreamingTV_Yes'],
                data['StreamingMovies_Yes'],
                data['tenure'],
                data['Contract_Two_year'],
                data['InternetService_DSL'],
                data['MultipleLines_No'],
                data['PaperlessBilling_No'],
                data['PaymentMethod_Credit_card'],
                data['TechSupport_Yes'],
                data['OnlineSecurity_Yes'],
                data['PhoneService_Yes'],
                data['Dependents_Yes']
            ]

            # Appeler la fonction de prédiction
            prediction_lr, prediction_rf, prediction_svm = make_churn_prediction(input_values)

            # Préparer les données à afficher dans le template
            context = {
                'form':form,
                'prediction_lr': prediction_lr,
                'prediction_rf': prediction_rf,
                'prediction_svm': prediction_svm
            }

            return render(request, 'pred/resultchurn.html', context)
    else:
        form = ChurnPredictionForm()

    return render(request, 'pred/predictchurn.html', {'form': form})

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"
    slug_url_kwarg = 'slug'

def blog(request):
    categories_with_count = Article.objects.values('category').annotate(post_count=Count('id'))
    context = {'articles':Article.objects.all(),
               'articles_ordered':Article.objects.order_by('-date_creation'),
               'categories_with_count': categories_with_count}
    return render(request, "blog/articles.html", context)

def article(request,slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request,"blog/article.html",{'article':article})