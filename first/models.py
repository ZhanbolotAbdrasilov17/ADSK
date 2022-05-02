from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    pass

class Clients(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="")
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    full_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    project_title = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    work_experience = models.CharField(max_length=200, null=True)
    education = models.CharField(max_length=200, null=True)
    achievements = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    announcement = models.CharField(max_length=200, null=True, blank=True, verbose_name='Анонс')
    image = models.ImageField(upload_to='news_images', verbose_name='Фото')
    text = models.TextField(verbose_name='Текст')
    author = models.CharField(max_length=200, verbose_name='Источник')

    def __str__(self):
        return self.title