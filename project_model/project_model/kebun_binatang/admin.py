from django.contrib import admin
from .models import Hewan, Kandang, Pengunjung, Penjaga

class HewanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'species', 'berat', 'umur']

class KandangAdmin(admin.ModelAdmin):
    list_display = ['nama', 'isi_kandang', 'luas_kandang']

class PenjagaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nomor_telepon', 'jadwal_jaga']

class PengunjungAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nomor_telepon', 'hari_berkunjung']


# Register your models here.
admin.site.register(Hewan, HewanAdmin)
admin.site.register(Kandang, KandangAdmin)
admin.site.register(Pengunjung, PengunjungAdmin)
admin.site.register(Penjaga, PenjagaAdmin)


