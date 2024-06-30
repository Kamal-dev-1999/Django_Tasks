from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.SignUp, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('landingpage/', views.landingpage, name='landingpage'),
]
