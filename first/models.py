from django.db import models

from django.db.models import QuerySet


class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=300, verbose_name="Должность")
    image = models.ImageField(null=True, blank=True, upload_to="doctors")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудники'
        ordering = ['full_name']


class EmDescription(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="descriptions")
    text = models.TextField(verbose_name="Описание")


class Projects(models.Model):
    project_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проекты'
        ordering = ['project_name']


class Portfolio(models.Model):
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="projects")
    project_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio_images', verbose_name='Фото', blank=True, null=True)
    text = models.TextField(verbose_name="Полное описание")

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = 'Портфолио'
        ordering = ['project_title']




class NewTechno(models.Model):
    project_title = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    text = models.TextField(verbose_name="Поле", blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = 'Новое_технологии'
        ordering = ['project_title']


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Новости")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="news")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новоcти'
        ordering = ['title']

    @classmethod
    def search_news(cls, value: str) -> QuerySet:
        return cls.objects.filter(
            models.Q(title__icontains=value) | models.Q(news_descriptions__text__icontains=value)
        )

    @classmethod
    def last_four_news(cls) -> QuerySet:
        return cls.objects.all().order_by('created_at')[:4]




class NewsPictures(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='news-images', verbose_name='Фото')

    def __str__(self):
        return self.news

    class Meta:
        verbose_name = 'Картинки новостей'



class FullDescription(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_descriptions")
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = 'Полное описание новостей'




class Partners(models.Model):
    partner_name = models.CharField(max_length=200, verbose_name="Название партнера")
    partner_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='partners_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = 'Партнёры'



class FullDescriptionNewTechno(models.Model):
    techno = models.ForeignKey(NewTechno, on_delete=models.CASCADE, related_name="new_techno_description")
    text = models.TextField(verbose_name="Текст_новых_технологий")


class Smi(models.Model):
    title = models.CharField(max_length=300, null=True)
    link = models.CharField(max_length=300, verbose_name="ссылка")
    image = models.ImageField(null=True, blank=True, upload_to="portals")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'СМИ о нас'
        ordering = ['title']


class PortFolioCompanies(models.Model):
    project_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio_images', verbose_name='Фото', blank=True, null=True)
    text = models.TextField(verbose_name="Полное описание")

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = 'Портфолио компаний'

class InternationalCongresses(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='international', verbose_name='Фото', blank=True, null=True)
    text = models.TextField(verbose_name="Полное описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Международные конгрессы'
        ordering = ['title']

class Quotes(models.Model):
    image = models.ImageField(upload_to='header', verbose_name='Фото', blank=True, null=True)
    text = models.CharField(max_length=200, null=True, blank=True)
    quote = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Цитаты'
        ordering = ['quote']

class ManagersQuotes(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    job_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='managers', verbose_name='Фото', blank=True, null=True)
    text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Цитаты менеджеров'
        ordering = ['full_name']

class VideoContent(models.Model):
    text = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='video_content', verbose_name='Фото', blank=True, null=True)
    video = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Видео контент'


class RezultatyOblastey(models.Model):
    region = models.CharField(max_length=200, null=True, blank=True)
    results = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = 'Результаты областей'








