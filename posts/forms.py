from django import forms 
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','email','phone_number','slug','banner']