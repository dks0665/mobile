from django.db import models

# Create your models here.

class Notice(models.Model):

    작성자 = models.CharField(null=True,max_length=30)

    작성일 = models.DateTimeField()

    제목 = models.CharField(null=True,max_length=100)

    내용 = models.TextField()