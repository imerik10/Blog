from django.urls import path
from .views import homepage,registration,product_detail,signin,log_out,create_post

urlpatterns = [
    path('',homepage,name='home'),
    path('blog/<int:id>',product_detail,name='detail'),
    path('reg/',registration,name='reg'),
    path('login/',signin,name='login'),
    path('logout/',log_out,name='logout'),
    path('create/',create_post,name='create')


]