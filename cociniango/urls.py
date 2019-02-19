"""cociniango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    #   Django Admin Site.
    path('admin/', admin.site.urls, name='admin'),
    #   Recetas.
    url(r'^', include ('apps.recetas.urls', namespace='receta')),
    # Registro.
    url(r'^registro/', include ('apps.registration.urls', namespace='registro')),
    # Inicio de sesión - Cerrar Sesión.
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Reseteo de contraseña.
    path('reset/password_reset',PasswordResetView.as_view(),
    {'template_name':'registration/password_reset_form.html','email_template_name':'registration/password_reset_email.html'},name="password_reset"),
    path('password_reset_done',PasswordResetDoneView.as_view(),{'template_name':'registration/password_reset_done.html'},name="password_reset_done"),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), {'template_name':'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(),{'template_name':'registration/password_reset_complete.html'},name="password_reset_complete"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
