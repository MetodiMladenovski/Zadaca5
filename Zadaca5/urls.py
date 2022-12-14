"""Zadaca5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LearnTradingSwiftly.views import index, beginnerLessons, advancedLessons, lesson, login, register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('beginnerLessons/', beginnerLessons, name="beginnerLessons"),
    path('advancedLessons/', advancedLessons, name="advancedLessons"),
    path('advancedLessons/lesson/<int:index>/', lesson, name='lesson'),
    path('beginnerLessons/lesson/<int:index>/', lesson, name='lesson'),
    path('login/', login, name="login"),
    path('register/', register, name="register"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
