# Generated by Django 2.1.2 on 2018-11-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuentinhaFood', '0004_auto_20181110_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagem_usuario',
            field=models.ImageField(upload_to='user_images'),
        ),
    ]