# Generated by Django 3.2.9 on 2022-06-28 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0013_auto_20220627_1605'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsImages',
            new_name='KartinkiNovostey',
        ),
        migrations.RenameModel(
            old_name='InternationalCongresses',
            new_name='MezhdunarodnyeKon',
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='Novosti',
        ),
        migrations.RenameModel(
            old_name='NewTechno',
            new_name='NovyeTehnologii',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Proekty',
        ),
        migrations.RenameModel(
            old_name='Media',
            new_name='Smi',
        ),
        migrations.RenameModel(
            old_name='Employee',
            new_name='Sotrudniki',
        ),
        migrations.RenameModel(
            old_name='Quotes',
            new_name='Tchitaty',
        ),
        migrations.RenameModel(
            old_name='ManagersQuotes',
            new_name='TchitatyMenedzherov',
        ),
    ]
