# Generated by Django 3.2.9 on 2022-07-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0020_auto_20220706_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MezhdunarodnyeKon',
            new_name='InternationalCongresses',
        ),
        migrations.RenameModel(
            old_name='Tchitaty',
            new_name='Quotes',
        ),
        migrations.AlterModelOptions(
            name='internationalcongresses',
            options={'ordering': ['title'], 'verbose_name': 'Международные конгрессы'},
        ),
        migrations.AlterModelOptions(
            name='portfoliocompanies',
            options={'verbose_name': 'Портфолио компаний'},
        ),
        migrations.AlterModelOptions(
            name='quotes',
            options={'ordering': ['quote'], 'verbose_name': 'Цитаты'},
        ),
    ]
