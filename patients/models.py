from django.db import models

class Dieseases(models.Model):
   illness=models.CharField(max_length=64)
   duration=models.IntegerField()





# Create your models here.
class Patient(models.Model):
    fullname=models.ForeignKey(Dieseases,on_delete=models.CASCADE,related_name="patients with this ill+")
    filenumber=models.IntegerField()
    address=models.ForeignKey(Dieseases,on_delete=models.CASCADE,related_name="location")
    def __str__(self):
      return f"{self.id}: {self.fullname}with file number {self.filenumber}"