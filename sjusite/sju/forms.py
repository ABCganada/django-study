from django import forms
from sju.models import Semester, Subjects

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['table', 'credits', 'grade']
        widgets = {
            'table': forms.TextInput(attrs={'class': 'form-control'}),
            'credits': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }
        lables = {
            'table': '시간표',
            'credits': '이수 학점',
            'grade' : '학점 평점',
        }

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['name', 'credit']
        labels = {
            'name': '과목 이름',
            'credit': '학점',
        }