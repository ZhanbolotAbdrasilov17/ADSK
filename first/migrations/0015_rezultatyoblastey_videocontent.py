# Generated by Django 3.2.9 on 2022-06-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0014_auto_20220628_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='RezultatyOblastey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('results', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('text_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('text_ky', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='video_content', verbose_name='Фото')),
                ('video', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
