from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    author = models.ForeignKey('auth.User', verbose_name='Автор', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Пост')


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])