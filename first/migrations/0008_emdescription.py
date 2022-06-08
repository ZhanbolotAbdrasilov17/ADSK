# Generated by Django 3.2.9 on 2022-06-08 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_auto_20220607_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emdescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='first.employee')),
            ],
        ),
    ]
