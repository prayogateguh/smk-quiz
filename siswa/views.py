from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Profile
from choice.models import Score


@login_required
def profile(request, pk):
    siswa = get_object_or_404(Profile, pk=pk)
    ujian = Score.objects.filter(user=pk)

    return render(request, 'siswa/profile.html', {'siswa': siswa, 'ujian': ujian,})


@login_required
def your_test(request, pk):
    ujian = Score.objects.filter(user=pk).order_by('-tanggal')[0]

    return render(request, 'siswa/your_test.html', {'ujian': ujian, })
