from distutils.command.upload import upload
from django.db import models

# Create your models here.

class destination(models.Model):
    desc=models.TextField()
    price =models.IntegerField()
    name= models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)