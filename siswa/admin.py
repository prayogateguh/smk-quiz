from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'nama_lengkap', 'nim', 'kelas', 'slug',)
    fields = ('user', 'nama_lengkap', 'nim', 'kelas',)
