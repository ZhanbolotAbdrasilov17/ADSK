# Generated by Django 3.2.9 on 2022-06-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_portfolio_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=200, verbose_name='Название партнера')),
                ('partner_description', models.TextField()),
                ('image', models.ImageField(upload_to='partners_images', verbose_name='Фото')),
            ],
        ),
    ]
