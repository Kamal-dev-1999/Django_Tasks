from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post  # Import the Post model from your models file
# we imoported listview and detailview which will simplfy the output in such a way that on cliccking the element we will be ablo to get the detailed view of the section
# Create your views here.


# # def Home(request):
#     return render(request, 'home.html',context={})

class HomeView(ListView):
    model=Post
    template_name='home.html'
    
class article_detail(DetailView):
    model=Post
    template_name='article_detail.html'
    
class add_post(CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__' #this will make all the avialible fields in the models.py avialbale 