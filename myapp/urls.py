from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('solution',views.solution,name="solution"),
    path('avis',views.avis,name="avis"),
    path('ecrireavis',views.ecrireavis,name="ecrireavis"),
    path('contact',views.contact,name="contact"),
    path('voiture',views.voiture,name='voiture'),
    path('telecommunication',views.telecommunication,name="telecommunication"),
    path('signup',views.signup,name='signup'),
    path('prediction',views.prediction_view,name='prediction_view'),



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 