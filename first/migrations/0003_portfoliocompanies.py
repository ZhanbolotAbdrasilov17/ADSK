# Generated by Django 3.2.9 on 2022-06-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20220622_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortFolioCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio_images', verbose_name='Фото')),
                ('text', models.TextField(verbose_name='Полное описание')),
            ],
        ),
    ]
