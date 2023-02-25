from django.db import models
from datetime import date 
# Create your models here.
class Save(models.Model):
    name = models.TextField()
    Phone = models.IntegerField()
    Email =models.EmailField()
    Date = models.DateField()
    Time = models.TimeField()
    Area=models.TextField()
    City=models.TextField()
    State=models.TextField()
    Postal_code=models.IntegerField()

  
   
    

