from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *
from manager.forms import *

def index(request):
    students = Student.objects.all() #データベースから取得
    return render(request, "index.html", {"students": students})

def change(request):
    students = Student.objects.all() #データベースから取得
    formset = RadioFormSet(request.POST or None)
    if request.method == "POST":
        formset.save() 
        print(formset)
    else:
        formset = RadioFormSet()
    return render(request, "change.html", {"students": students, "formset": formset})

# Create your views here.
