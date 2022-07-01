# Generated by Django 3.2.9 on 2022-06-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0010_auto_20220624_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='news-images', verbose_name='Фото')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.news')),
            ],
        ),
    ]