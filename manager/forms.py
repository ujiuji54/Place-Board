from django import forms
from django.forms import formset_factory
from django.contrib.admin import widgets
import os

from .models import Student 

CHOICE = {
    ("0","在室"),
    ("1","教室"),
    ("2","校内"),
    ("3","自宅"),
}

class RadioForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("place",)
        widgets ={
            "place" : forms.RadioSelect,
        }

RadioFormSet = formset_factory(RadioForm)
