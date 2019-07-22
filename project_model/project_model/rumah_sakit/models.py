from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    bidang = models.CharField(max_length=100)
    jadwal_praktek = models.DateField()


class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    alamat = models.TextField()
    keluhan = models.TextField()


class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.CharField(max_length=20)
    kumpulan_obat = models.CharField(max_length=255)


class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.CharField(max_length=255)
    khasiat = models.CharField(max_length=255)


