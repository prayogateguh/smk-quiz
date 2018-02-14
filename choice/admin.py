from django.contrib import admin
from .models import Exam, Question, Score


admin.site.register(Exam)
admin.site.register(Question)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'mata_pelajaran', 'score', 'kkm', 'tanggal')

admin.site.register(Score, ScoreAdmin)