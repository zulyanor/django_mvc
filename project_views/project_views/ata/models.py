from django.db import models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)
    tanggal = models.DateField()
    comment = models.CharField(max_length=255)
    desc = models.TextField()

class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    quotes = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    quotes = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)