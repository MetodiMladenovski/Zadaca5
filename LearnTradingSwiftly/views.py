from django.shortcuts import render, get_object_or_404
from .models import Lesson
from django.db.models import Q


# Create your views here.

def index(request):
	queryset = Lesson.objects.all()
	context = {"lessons": queryset}
	return render(request, 'index.html', context=context)

def beginnerLessons(request):
	queryset = Lesson.objects.filter(~Q(title='logo')).filter(isAdvanced=False).all()
	context = {"lessons": queryset}
	return render(request, "beginnerLessons.html", context=context)

def advancedLessons(request):
	queryset = Lesson.objects.filter(~Q(title='logo')).filter(isAdvanced=True).all()
	context = {"lessons": queryset}
	return render(request, "advancedLessons.html", context=context)

def lesson(request, index):
	lesson = get_object_or_404(Lesson, id=index)
	context = {'lesson': lesson,}
	return render(request, "lesson.html", context)


def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')