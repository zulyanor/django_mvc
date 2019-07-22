from django.contrib import admin
from.models import Direksi, Mentee, Mentor, MataPelajaran, Challenge, LiveCode

class DireksiAdmin(admin.ModelAdmin):
    list_display = ['nama_lengkap', 'no_telepon', 'jabatan']

class MenteeAdmin(admin.ModelAdmin):
    list_display = ['nama_lengkap', 'no_telepon', 'no_absen', 'nilai_rata']

class MentorAdmin(admin.ModelAdmin):
    list_display = ['nama_lengkap', 'no_telepon', 'mata_pelajaran']

class MataPelajaranAdmin(admin.ModelAdmin):
    list_display = ['nama_pelajaran', 'jadwal_dimulai', 'jadwal_berakhir']

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['nama_challenge', 'banyak_soal', 'bobot_nilai', 'mata_pelajaran']

class LiveCodeAdmin(admin.ModelAdmin):
    list_display = ['nama_live_code', 'banyak_soal', 'bobot_nilai', 'tanggal_pelaksanaan', 'mata_pelajaran']


# Register your models here.
admin.site.register(Direksi, DireksiAdmin)
admin.site.register(Mentee, MenteeAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(MataPelajaran, MataPelajaranAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(LiveCode, LiveCodeAdmin)