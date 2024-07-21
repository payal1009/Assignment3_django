from django.db import models

class modelClass(models.Model):
    i=models.IntegerField()
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    date=models.DateField()
    status=models.BooleanField(default=None)
    
    