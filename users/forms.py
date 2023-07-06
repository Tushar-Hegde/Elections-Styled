from django import forms
from .models import BasicInfo

class RegisterForm(forms.ModelForm):
    survey_name = forms.CharField(widget = forms.TextInput(attrs={'class':'special'}), label = '')
    survey_id = forms.CharField(widget = forms.TextInput(attrs={'class':'special'}), label = '')
    class Meta():
        model=BasicInfo
        fields=['survey_name','survey_id']