from django.contrib import admin

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus.tables import Table

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nama_lengkap', 'nim', 'kelas', 'slug', 'post_pic',)
    fields = ('user', 'nama_lengkap', 'nim', 'kelas', 'sudah_ujian', 'post_pic',)
