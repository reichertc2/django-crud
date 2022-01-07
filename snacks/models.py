from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    descrition = models.CharField(max_length=256)