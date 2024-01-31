from django.db import models

# Create your models here.
class bus_details(models.Model):
    bus_name=models.CharField(max_length=50)
    bus_number=models.IntegerField()
    bus_rotues=models.CharField(max_length=50)
    bus_Start_timmigs=models.DateTimeField(blank=True,default="2006-12-27 10:20:50")
    bus_end_timmigs=models.DateTimeField(blank=True,default="2006-12-27 16:30:10")
    bus_fare=models.IntegerField()

    def __str__(self):
        return self.bus_name
    
