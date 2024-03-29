"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('change_password', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path("password_change_done", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_change_done.html"),name='password_reset_complete'),

    path("",include(('myapp.urls','myapp'),namespace='myapp')),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
