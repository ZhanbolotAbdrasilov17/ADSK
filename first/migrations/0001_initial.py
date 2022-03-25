# Generated by Django 3.2.9 on 2022-03-24 13:00

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_experience', models.CharField(max_length=200, null=True)),
                ('education', models.CharField(max_length=200, null=True)),
                ('achievements', models.CharField(max_length=200, null=True)),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.clients')),
                ('project_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='first.project')),
            ],
        ),
    ]
