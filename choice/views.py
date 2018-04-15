from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from rest_framework import viewsets

from .models import Exam, Question, Score
from .serializer import ExamSerializer, QuestionSerialzer

from siswa.models import Profile


#welcome screen
def welcome(request):
    if request.user.is_authenticated():
        siswa = get_object_or_404(Profile, user=request.user)
        return render(request, "exam.html", {'siswa': siswa, })
    return render(request, "login.html")


@login_required()
def upload_score(request):
    if request.method == 'POST':
        if 'test-score' in request.POST:
            score = request.POST['test-score']
        else:
            score = 0
        s = Score()
        user = request.POST.get("user")
        exam = request.POST.get("test-name")
        lulus = request.POST['lulus']
        s.user = User.objects.get(pk=user)
        s.mata_pelajaran = Exam.objects.get(pk=exam)
        print("print:"+lulus)
        # s.lulus = bool(int(lulus))
        s.score = score
        s.save()
        p = get_object_or_404(Profile, user=user)
        p.sudah_ujian = True
        p.save()
        return HttpResponseRedirect(reverse('siswa:result', args=(s.user.pk,)))


#viewsets for rest_framework
class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialzer


class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all().order_by('-tanggal')[:1]
    serializer_class = ExamSerializer


class ExamQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerialzer
    queryset = Question.objects.filter(exam_id = 1)
    def get_queryset(self):
        return Question.objects.filter(exam_id=self.kwargs.get('pk'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
