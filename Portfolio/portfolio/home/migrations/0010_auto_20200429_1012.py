# Generated by Django 3.0.5 on 2020-04-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200429_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
