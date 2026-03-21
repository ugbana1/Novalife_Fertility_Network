from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def posts_list(request):
    posts  =Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts})




def post_page(request,slug):
    post  =Post.objects.get(slug=slug)
    return render(request,'posts/post_page.html',{'post':post})
   

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method =="POST":
        form =forms.CreatePost(request.POST,request.FILES) 
        if form.is_valid():
            newpost = form.save(commit= False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')

    
    else:
         form=forms.CreatePost()
    return render(request,'posts/post_new.html',{'form':form})

@login_required(login_url="/users/login/")
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        send_mail(
            subject=f"Contact Form Message from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['okekeisaacs@gmail.com','wonderworld1tv@gmail.com','fertilitynetworknovalife@gmail.com'],
        )

        return render(request, 'posts/contact.html', {'success': True})

    return render(request, 'posts/contact.html')