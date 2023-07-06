from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from users import views as user_views
from .forms import QuestionForm

# Create your views here.

'''def home(request):
    form = QuestionForm(request.POST)
    s_id = user_views.s_id
    return render(request, 'questionnaire/home.html', {'form':form})'''
    
def home(request):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else: # called before the if condition
        form = QuestionForm
        return render(request, 'questionnaire/home.html', {'form':form})

