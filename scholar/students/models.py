from django.db import models
class User(models.Model):
    emaIl=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    

