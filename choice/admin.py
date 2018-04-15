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
    list_display = ('name', 'guru', 'kkm', 'tanggal')


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'mata_pelajaran', 'score', 'lulus', )
    actions = ['convert_pdf']

    def convert_pdf(self, request, queryset):
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.platypus.tables import Table
        from django.http import HttpResponse

        cm = 2.54
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=hasil_nilai.pdf'


        elements = []

        doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)

        data = [["Nama Siswa", "Mata Pelajaran", "Score", "Lulus"],]

        for s in queryset:
            data.append([s.user, s.mata_pelajaran, s.score, s.lulus])
        table = Table(data)
        elements.append(table)
        doc.build(elements) 
        return response
