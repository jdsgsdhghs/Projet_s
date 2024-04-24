from django.db import models

# Create your models here..
class Trainsncf(models.Model) :
    TrainID = models.AutoField(primary_key=True)
    City = models.CharField(max_length = 200)
    Departure_Time = models.TimeField(max_length = 50)
    Arrival_Time = models.TimeField(max_length = 50)
   