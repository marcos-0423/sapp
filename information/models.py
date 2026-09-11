from django.db import models  # pyright: ignore[reportMissingModuleSource]

# Create your models here.
class Information(models.Model):
    patientname = models.CharField(max_length=64)
    age = models.IntegerField()
    sickness = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.patientname} - {self.age} - {self.sickness}"


class Doctors(models.Model):
    doctorname = models.CharField(max_length=64)
    specialization = models.CharField(max_length=128)
    doctors=models.ManyToManyField(Information, related_name='doctors')
    def __str__(self):
        return f"{self.doctorname} - {self.specialization}"