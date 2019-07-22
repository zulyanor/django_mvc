from django.contrib import admin
from .models import Dokter, Pasien, Obat, Resep

class DokterAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'bidang', 'jadwal_praktek']

class PasienAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'nomor_telepon', 'alamat', 'keluhan']

class ResepAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'total_harga', 'kumpulan_obat']

class ObatAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'kandungan', 'khasiat']


# Register your models here.
admin.site.register(Dokter, DokterAdmin)
admin.site.register(Pasien, PasienAdmin)
admin.site.register(Resep, ResepAdmin)
admin.site.register(Obat, ObatAdmin)

