# Generated by Django 3.2.9 on 2022-07-06 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0018_auto_20220706_1409'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KartinkiNovostey',
            new_name='NewsPictures',
        ),
        migrations.AlterModelOptions(
            name='newspictures',
            options={'verbose_name': 'Картинки новостей'},
        ),
    ]
