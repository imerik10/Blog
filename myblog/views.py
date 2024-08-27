from django.shortcuts import render,get_object_or_404,redirect
from . import models,forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required



# Create your views here.
def homepage(request):
    blogs = models.Blogs.objects.all()
    return render(request,'home.html',{'bloglar':blogs})

def product_detail(request,id):
    blog = get_object_or_404(models.Blogs,id=id)
    return render(request,'detail.html',{'blog':blog})

def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'reg.html',{'form':form})

def signin(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')


@login_required

def create_post(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.BlogForm()
    return render(request,'create_post.html',{'form':form})