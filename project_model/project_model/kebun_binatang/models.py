from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species = models.CharField(max_length=250)
    berat = models.CharField(max_length=10)
    umur = models.CharField(max_length=5)

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.CharField(max_length=255)
    luas_kandang = models.CharField(max_length=20)

class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    jadwal_jaga = models.DateField()

class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    hari_berkunjung = models.DateTimeField()
