from django.db import models

# Create your models here.

class Main(models.Model):
    완성사진 = models.ImageField(upload_to='recipeImages/')

    이름 = models.CharField(null=True,max_length=30)

    재료 = models.CharField(null=True,max_length=100)

    레시피1_사진 = models.ImageField(upload_to='recipeImages/')
    레시피1 = models.TextField()

    레시피2_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피2 = models.TextField(blank=True)

    레시피3_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피3 = models.TextField(blank=True)
    
    레시피4_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피4 = models.TextField(blank=True)
    
    레시피5_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피5 = models.TextField(blank=True)

    레시피6_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피6 = models.TextField(blank=True)

    레시피7_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피7 = models.TextField(blank=True)

    레시피8_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피8 = models.TextField(blank=True)

    레시피9_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피9 = models.TextField(blank=True)

    레시피10_사진 = models.ImageField(blank=True, upload_to='recipeImages/')
    레시피10 = models.TextField(blank=True)

