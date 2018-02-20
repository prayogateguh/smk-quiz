from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.profile, name="profile"),
    url(r'^(?P<pk>\d+)/results/$', views.your_test, name="result"),
    # url(r'^pdf/$', views.convert_pdf, name="convert_pdf"),
]
