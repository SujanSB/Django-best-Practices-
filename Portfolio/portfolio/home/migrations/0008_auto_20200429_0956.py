# Generated by Django 3.0.5 on 2020-04-29 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Blog title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latestwork',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Work title'),
            preserve_default=False,
        ),
    ]
