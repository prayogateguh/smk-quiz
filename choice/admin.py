from django.contrib import admin
from .models import Exam, Question, Score


class QuestionInline(admin.StackedInline):
    model = Question
    fieldsets = (
                    ('+',
                    {
                        'classes': ('collapse',),
                        'fields': (
                            'question',
                            'option1',
                            'option2',
                            'option3',
                            'option4',
                            'answer'
                        ),
                    }
                    ),

                )
    
    extra = 0


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name', 'user')


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'mata_pelajaran', 'score', 'kkm', 'tanggal')