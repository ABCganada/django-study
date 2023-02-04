from django import forms
from pybo.models import Question, Answer

# QuestionForm은 Question 모델과 연결된 폼.
# 속성으로 Question 모델의 subject와 content를 사용.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        lables = {
            'content': '답변내용',
        }