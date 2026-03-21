from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=75)
    body=models.TextField()
    email=models.EmailField(max_length=254,unique=True,blank=True,null=True)
    phone_number = PhoneNumberField(region="US", blank=True)
    slug=models.SlugField()
    date =models.DateTimeField(auto_now_add=True)
    banner =models.ImageField(default='fallback.jpg',blank=True)
    author =models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    