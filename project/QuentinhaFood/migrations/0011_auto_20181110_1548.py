# Generated by Django 2.1.2 on 2018-11-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuentinhaFood', '0010_auto_20181110_1526'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='estabelecimento',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='cnpj',
            field=models.CharField(max_length=100),
        ),
    ]
