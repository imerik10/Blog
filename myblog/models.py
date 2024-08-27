from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=250,verbose_name='Название категории: ')
    slug = models.SlugField(verbose_name='Слэг категории: ',max_length=255,)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.category_name


class Blogs(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    title = models.CharField(max_length=250,verbose_name='Название поста: ')
    text = models.TextField(verbose_name='Текст поста: ')
    image1 = models.ImageField(verbose_name='1 картинка для поста: ',blank=True, null=True)
    image2 = models.ImageField(verbose_name='2 картинка для поста(не обьязательно): ',blank=True, null=True)
    image3 = models.ImageField(verbose_name='3 картинка для поста(не обьязательно): ',blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
    
    def __str__(self):
        return self.title

