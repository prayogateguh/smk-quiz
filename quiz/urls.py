"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from choice import views


urlpatterns = [
    # apps urls conf
    url(r'^quiz/', include('choice.urls', namespace='choice', app_name='choice')),
    url(r'^siswa/', include('siswa.urls', namespace='siswa', app_name='siswa')),
    url(r'^$', views.welcome, name="home"),

    # admin app
    url(r'^admin/', admin.site.urls),
]
