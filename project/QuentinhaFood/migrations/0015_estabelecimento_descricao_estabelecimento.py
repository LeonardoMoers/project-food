# Generated by Django 2.1.2 on 2018-11-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuentinhaFood', '0014_auto_20181112_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='descricao_estabelecimento',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
