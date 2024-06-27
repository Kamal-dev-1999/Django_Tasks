from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),#we used class based view 
    path('article/<int:pk>',views.article_detail.as_view(),name='article_detail'),
    path('add_post/',views.add_post.as_view(),name='add_post'),
]