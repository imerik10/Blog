from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('blog/<int:id>',views.product_detail,name='detail'),


]