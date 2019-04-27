from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
     title=models.CharField(max_length=120)
     user = models.OneToOneField(get_user_model(),
            on_delete=models.CASCADE)
     content=models.TextField()
     publishing_date=models.DateTimeField(auto_now_add=True)
     image=models.FileField(null=True,blank=True)

     def __str__(self):
         return self.title
     def get_absolute_url(self):
         return reverse('post:detail',kwargs={'id':self.id})


     class Meta:
         ordering=['-publishing_date']
     
            