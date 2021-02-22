from django.db import models

# Create your models here.
#About ko lagi MOdel
class About(models.Model):
    short_description=models.TextField()
    description=models.TextField()
    image =models.ImageField(upload_to='pics')
    age =models.IntegerField()

    class meta:
        verbose_name ="About me"
        verbose_name_plural ="About me"

    def __str__(self):
        return "About me"
    
#Service Models Haru yeta
class Services(models.Model):
    name =models.CharField(max_length=100,verbose_name="Service name")
    description =models.TextField(verbose_name="About services")

    def __str__(self):
        return self.name
        
    
#Portfolio Work haru ko lagi
class LatestWorkWD(models.Model):
    # title= models.CharField(max_length=100,verbose_name="Work title")
    # CLASS_NAME =(
    #              ('A','All'),
    #              ('P','Photoshop'),
    #              ('K','Branding'),
    #              ('C','Fashion'),
    # )
    # class_name=models.CharField(max_length=1,choices=CLASS_NAME)
    image =models.ImageField(upload_to="pics")


    # def __str__(self):
    #     return self.title,class_name


# diferent work anusar ka
class LatestWorkP(models.Model):
    image =models.ImageField(upload_to="pics")

class LatestWorkK(models.Model):
    image =models.ImageField(upload_to="pics")



class Testimonials(models.Model):
    name =models.CharField(max_length=100,verbose_name="Client name")
    description =models.TextField(verbose_name="Client on me")
    img =models.ImageField( upload_to="pics", default="default.png")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name =models.CharField(max_length=50)
    email =models.EmailField(max_length=254) 
    desc =models.TextField()
    date = models.DateField()
    


class Blog(models.Model):
    date =models.DateField(auto_now_add=True)
    title= models.CharField(max_length=100,verbose_name="Blog title")
    desc =models.TextField()
    short_desc=models.CharField(max_length=50)
    image = models.ImageField( upload_to="pics")

    
    

    
    