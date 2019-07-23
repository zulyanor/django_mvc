from django.contrib import admin
from .models import Mentee, Mentor, Blog

# Register your models here.
class MenteeAdmin(admin.ModelAdmin):
    list_display = ['nama', 'quotes', 'profile_pic']

class MentorAdmin(admin.ModelAdmin):
    list_display = ['nama', 'experience', 'quotes', 'profile_pic']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['judul', 'gambar', 'tanggal', 'comment', 'desc']


admin.site.register(Mentee, MenteeAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Blog, BlogAdmin)
