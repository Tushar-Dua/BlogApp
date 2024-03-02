from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(
        max_length=20,
        null=True,
        blank=False
    )
    description = models.CharField(max_length=100,null=True,blank=False)
