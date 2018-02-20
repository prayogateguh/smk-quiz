from django.conf.urls import include, url

from . import views
from rest_framework import routers

from .views import ExamQuestionViewset, ExamViewset, QuestionViewset

router = routers.SimpleRouter()
router.register(r'question', QuestionViewset)
router.register(r'exam', ExamViewset)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^score/', views.upload_score, name="upload_score"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
