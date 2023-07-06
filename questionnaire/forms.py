from django import forms
from .models import Surveys

class QuestionForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    identity=forms.CharField(max_length=50)
    questions=forms.CharField(max_length=1000)
    class Meta:
        model = Surveys
        fields = ["name","identity","questions"]