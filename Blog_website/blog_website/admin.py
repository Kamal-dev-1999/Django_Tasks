from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
#using this we register the admin to make changes to the site and also add or delete blog