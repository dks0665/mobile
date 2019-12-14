from django.db import models

# Create your models here.
class Main(models.Model):
    title =  models.CharField(max_length=255)
    pup_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    character = models.CharField(max_length=300)