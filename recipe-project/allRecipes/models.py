from django.db import models

# Create your models here.
class allRecipes(models.Model):
    완성사진 = models.ImageField(upload_to="images/")

    이름 = models.CharField(max_length=30)

    재료 = models.CharField(max_length=100)

    레시피1_사진 = models.ImageField(upload_to='recipe_images/')
    레시피1 = models.TextField()

    레시피2_사진 = models.ImageField(blank=True, upload_to='recipe_images/')
    레시피2 = models.TextField(blank=True)

    레시피3_사진 = models.ImageField(blank=True, upload_to='recipe_images/')
    레시피3 = models.TextField(blank=True)
    
    레시피4_사진 = models.ImageField(blank=True, upload_to='recipe_images/')
    레시피4 = models.TextField(blank=True)
    
    레시피5_사진 = models.ImageField(blank=True, upload_to='recipe_images/')
    레시피5 = models.TextField(blank=True)