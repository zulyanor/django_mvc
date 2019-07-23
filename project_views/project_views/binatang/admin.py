from django.contrib import admin
from .models import Hewan

# Register your models here.
class HewanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'species']


admin.site.register(Hewan, HewanAdmin)