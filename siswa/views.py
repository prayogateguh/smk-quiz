from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from choice.models import Score
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus.tables import Table

from .models import Profile


@login_required
def profile(request, pk):
    siswa = get_object_or_404(Profile, pk=pk)
    ujian = Score.objects.filter(user=pk).order_by('-tanggal')

    return render(request, 'siswa/profile.html', {'siswa': siswa, 'ujian': ujian,})


@login_required
def your_test(request, pk):
    try:
        ujian = Score.objects.filter(user=pk).order_by('-tanggal')[0]
    except:
        ujian = None

    return render(request, 'siswa/your_test.html', {'ujian': ujian, })


# @login_required
# def convert_pdf(modeladmin, request, queryset):
#     cm = 2.54
#     response = HttpResponse(mimetype='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

#     elements = []

#     doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)

#     data=[(1,2),(3,4)]
#     table = Table(data, colWidths=270, rowHeights=79)
#     elements.append(table)
#     doc.build(elements) 
#     return response
