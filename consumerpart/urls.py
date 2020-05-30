"""consumerpart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from monitoring.views import (
    oldhome,
    home,
    about,
    contact,
    HomeView,
    AboutView,
    ContactView,
    ConsumerView,
    ConsumerDetailView,
    ConsumerCreateView,
    Consumingstart,
    Consumingstop,
    QueueView,
    QueueCreateView,
    QueueDetailView,
    QueuDelete,
    ConsumerDelete,
    monitoringView,
    )
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('old_home/',oldhome),
    path('F', home),
    path('Fabout/', about),
    path('Fcontact/', contact),
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('static-web/',TemplateView.as_view(template_name="Static.html")),
    path('consumer/', ConsumerView.as_view()),
    path('consumer/<slug:slug>/', ConsumerDetailView.as_view()),
    path('consumer/add-new', ConsumerCreateView.as_view()),
    path('consumer/<slug:slug>/start', Consumingstart),
    path('consumer/<slug:slug>/stop', Consumingstop),
    path('queue/', QueueView.as_view()),
    path('queue/add-new', QueueCreateView.as_view()),
    path('queue/<slug:slug>/', QueueDetailView.as_view()),
    path('queue/<slug:slug>/delete', QueuDelete),
    path('consumer/<slug:slug>/delete', ConsumerDelete),
    path('monitoring/', monitoringView.as_view() ),

    
]
