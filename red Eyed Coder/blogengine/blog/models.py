from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150,db_index=True)
    slug =models.SlugField(max_length=150,unique=True)
    body =models.TextField(blank=True,db_index=True)
    date_pub =models.DateTimeField(auto_now_add=True)
    tags =models.ManyToManyField('Tag',blank =True ,related_name='posts')

    def __str__(self):
        return self.title



class Tag(models.Model):
    title =models.CharField(max_length=150)
    slug =models.SlugField(max_length=150,unique=True)

    def __str__(self):
        return self.title