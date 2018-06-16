from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *

def index(request):
    students = Student.objects.all() #データベースから取得
    return render(request, "index.html", {"students": students})

def change(request):
    students = Student.objects.all() #データベースから取得
    return render(request, "change.html", {"students": students})

# Create your views here.
