from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.
def homepage(request):
    blogs = models.Blogs.objects.all()
    return render(request,'home.html',{'bloglar':blogs})

def product_detail(request,id):
    blog = get_object_or_404(models.Blogs,id=id)
    return render(request,'detail.html',{'blog':blog})