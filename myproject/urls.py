"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('second/',include('second.urls')),
    path('blog_website/', include('blog_website.urls')),
    path('Authentication/', include('Authentication.urls')),
    path('Authentication/',include('django.contrib.auth.urls')),
    path('calender/',include('my_calender.urls')),
    path('polling/',include('polls.urls')),
    path('receipe/',include('recipeapp.urls')),
    path('rest_app/',include('rest_api_app.urls')),
    # path('api-auth/', include('rest_framework.urls'))
    path('crud/',include('CRUD.urls')),
    path('restapp/',include('restapp2.urls')),
    path('jwt-auth/',include('jwt_auth.urls')),
    
]
