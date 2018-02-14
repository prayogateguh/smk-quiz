from django.conf.urls import include, url

from . import views
from rest_framework import routers

from .views import ExamQuestionViewset, ExamViewset, QuestionViewset

router = routers.SimpleRouter()
router.register(r'question', QuestionViewset)
router.register(r'exam', ExamViewset)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.welcome, name="welcome"),
    url(r'^create/', views.create_user, name="create_user"),
    url(r'^validate_login/', views.log_in, name="log_user"),
    url(r'^add_exam/', views.add_exam, name="add_exam"),
    url(r'^add_question/', views.add_question, name="add_question"),
    url(r'^test', views.get_data, name="getdata"),
    url(r'^score/', views.upload_score, name="upload_score"),
    url(r'^logout', views.log_out, name="log_out"),
]
