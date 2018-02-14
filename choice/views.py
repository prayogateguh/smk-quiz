from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from rest_framework import viewsets

from .models import Exam, Question, Score
from .serializer import ExamSerializer, QuestionSerialzer


#welcome screen
def welcome(request):
    if request.user.is_authenticated():
        return render(request, "exam.html")
    return render(request, "index.html")

@login_required()
def get_data(request):
    return render(request,"exam.html")


#view for creating user
def create_user(request):
    if request.method == 'POST':
        name =  request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(name,email,password)
    return render(request, "index.html")

#view for logging in
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password  = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse("success")
            else:
                return HttpResponse("disabled account")
        else:
            return HttpResponse("invalid credentials")
@login_required()
def log_out(request):
    logout(request)
    return render(request, "index.html")

@login_required()
def add_exam(request):
    if request.method == 'POST':
        exam_name = request.POST.get("exam_name")
        user = request.POST.get("user")
        exam = Exam()
        exam.name = exam_name
        exam.user = User.objects.get(pk=user)
        exam.save()
        return HttpResponse(exam.id)

@login_required()
def add_question(request):
    if request.method == "POST":
        question  = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        answer = request.POST.get("answer")
        exam = request.POST.get("exam")
        q = Question()
        q.question = question
        q.option1 = option1
        q.option2 = option2
        q.option3 = option3
        q.option4 = option4
        q.answer = answer
        q.exam = Exam.objects.get(pk=int(exam))
        q.save()
        return HttpResponse("success")

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
        s.user = User.objects.get(pk=user)
        s.mata_pelajaran = Exam.objects.get(pk=exam)
        s.kkm = 75
        s.score = score
        s.save()
        return redirect('home')


#viewsets for rest_framework
class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialzer


class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerialzer
    queryset = Question.objects.filter(exam_id = 1)
    def get_queryset(self):
        return Question.objects.filter(exam_id=self.kwargs.get('pk'))
