from django import forms
from .models import *
from . import services
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'})
        }

class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'})
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields= "__all__"
        widgets = {
        "first_name":forms.TextInput(attrs={'class':'form-control'}),
        "last_name":forms.TextInput(attrs={'class':'form-control'}),
        "age":forms.NumberInput(attrs={'class':'form-control'}),
        "subject":forms.Select(attrs={'class':'form-control'}),
        "kafedra":forms.Select(attrs={'class':'form-control'}),
        }
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'}),
        "faculty":forms.Select(attrs={'class':'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= "__all__"
        widgets = {
        "first_name":forms.TextInput(attrs={'class':'form-control'}),
        "last_name":forms.TextInput(attrs={'class':'form-control'}),
        "age":forms.NumberInput(attrs={'class':'form-control'}),
        "group":forms.Select(attrs={'class':'form-control'}),
        "image": forms.FileInput(attrs={'class': 'form-control'})}