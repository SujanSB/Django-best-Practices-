# Generated by Django 3.0.5 on 2020-04-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonials',
            name='image',
        ),
        migrations.AddField(
            model_name='testimonials',
            name='img',
            field=models.ImageField(default='default.png', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='latestwork',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
