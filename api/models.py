from django.db import models
from django.contrib.auth.models import AbstractUser

#* USER MODEL

class User(AbstractUser):
  username = None
  
  name = models.CharField(max_length= 100)
  email = models.EmailField(unique= True)
  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name"]
  
  
#* PATIENT MODEL

class Patient(models.Model):
  user = models.ForeignKey(User, on_delete= models.CASCADE)
  name = models.CharField(max_length= 100)
  age = models.PositiveIntegerField()
  gender = models.CharField(max_length= 20)
  address = models.TextField()
  phone = models.CharField(max_length=15)
  
  def __str__(self):
    return self.name
  
#* DOCTOR MODEL

class Doctor(models.Model):
  name = models.CharField(max_length= 100)
  specialization = models.CharField(max_length= 120)
  email = models.EmailField(unique= True)
  phone = models.CharField(max_length= 15)
  
  def __str__(self):
    return self.name
  
#* MAPPING MODEL

class Mapping(models.Model):
  patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
  doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
  
  def __str__(self):
    return f"{self.patient.name} --> {self.doctor.name}"