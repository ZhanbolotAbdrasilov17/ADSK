# Generated by Django 3.2.9 on 2022-06-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_quotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='header', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
