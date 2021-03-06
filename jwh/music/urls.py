"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from music.views import list_select, list_same, list_dam,List

app_name = 'music'

urlpatterns = [
    path('list_select', list_select.as_view(), name='list_select'),
    path('list_same', list_same.as_view(), name='list_same'),
    path('list_dam', list_dam.as_view(), name='list_dam'),
    path('list',List.as_view(), name ="list"),
]
