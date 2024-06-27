from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    #define the things we want in our site
    title=models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #using the models.CASCADE if we delete any particular user then all the associated files /blogs /data of the user will be deleted from the databse
    body=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + '  |  ' + str(self.author) #we converted the author to a string so that we can concate it with the title which is already a string
    #this will display the author name and the blog title it uploaded 
    