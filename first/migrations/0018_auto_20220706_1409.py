# Generated by Django 3.2.9 on 2022-07-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0017_auto_20220706_1402'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Novosti',
            new_name='News',
        ),
        migrations.RenameModel(
            old_name='NovyeTehnologii',
            new_name='NewTechno',
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['title'], 'verbose_name': 'Новоcти'},
        ),
        migrations.AlterModelOptions(
            name='newtechno',
            options={'ordering': ['project_title'], 'verbose_name': 'Новое_технологии'},
        ),
    ]