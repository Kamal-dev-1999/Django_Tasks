from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser #we use Abstractuser model to extend the users in django other than the admin 





#custum user model

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    password=models.CharField(max_length=100) 
    USERNAME_FIELD = "email" #we added the inbuilt  username method of django login system and made the email itself as the username
    REQUIRED_FIELDS = []