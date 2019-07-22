from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    no_telp = models.CharField(max_length=17)

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    email =  models.CharField(max_length=50)
    no_telp = models.CharField(max_length=17)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)



    