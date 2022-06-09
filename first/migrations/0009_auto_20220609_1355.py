# Generated by Django 3.2.9 on 2022-06-09 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_emdescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
