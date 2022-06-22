from django.db import models

from django.db.models import QuerySet


class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=300, verbose_name="Должность")
    image = models.ImageField(null=True, blank=True, upload_to="doctors")

    def __str__(self):
        return self.full_name


class EmDescription(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="descriptions")
    text = models.TextField(verbose_name="Описание")


class Projects(models.Model):
    project_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.project_name


class Portfolio(models.Model):
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="projects")
    project_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio_images', verbose_name='Фото', blank=True, null=True)
    text = models.TextField(verbose_name="Полное описание")

    def __str__(self):
        return self.project_title


class NewTechno(models.Model):
    project_title = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    text = models.TextField(verbose_name="Поле", blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.project_title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Новости")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="news")

    def __str__(self):
        return self.title

    @classmethod
    def search_news(cls, value: str) -> QuerySet:
        return cls.objects.filter(
            models.Q(title__icontains=value) | models.Q(news_descriptions__text__icontains=value)
        )

    @classmethod
    def last_four_news(cls) -> QuerySet:
        return cls.objects.all().order_by('created_at')[:4]


class FullDescription(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_descriptions")
    text = models.TextField(verbose_name="Текст")


class Partners(models.Model):
    partner_name = models.CharField(max_length=200, verbose_name="Название партнера")
    partner_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='partners_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.partner_name


class FullDescriptionNewTechno(models.Model):
    techno = models.ForeignKey(NewTechno, on_delete=models.CASCADE, related_name="new_techno_description")
    text = models.TextField(verbose_name="Текст_новых_технологий")


class Media(models.Model):
    title = models.CharField(max_length=300, null=True)
    link = models.CharField(max_length=300, verbose_name="ссылка")
    image = models.ImageField(null=True, blank=True, upload_to="portals")

    def __str__(self):
        return self.title


class PortFolioCompanies(models.Model):
    project_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio_images', verbose_name='Фото', blank=True, null=True)
    text = models.TextField(verbose_name="Полное описание")

    def __str__(self):
        return self.project_title

class InternationalCongresses(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='international', verbose_name='Фото', blank=True, null=True)
    text = models.TextField(verbose_name="Полное описание")

    def __str__(self):
        return self.title



