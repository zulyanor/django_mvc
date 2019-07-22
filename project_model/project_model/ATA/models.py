from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=100)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)
    no_absen = models.CharField(max_length=3)
    nilai_rata = models.CharField(max_length=3)

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=20)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    
class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.CharField(max_length=2)
    bobot_nilai = models.CharField(max_length=5)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    
class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.CharField(max_length=3)
    bobot_nilai = models.CharField(max_length=5)
    tanggal_pelaksanaan = models.DateTimeField()
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
