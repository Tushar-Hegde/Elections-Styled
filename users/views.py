from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.

def register(request):
    global s_id
    if request.method=='POST': # trying to input data, called once signup is clicked
        form=RegisterForm(request.POST) # request.POST in brackets means data is being sent to the user creation form
        if form.is_valid():
            form.save()
            s_id = form.cleaned_data['survey_id']
        return redirect('/ElectionCode/home')
    else: # called before the if condition
        form = RegisterForm()
        return render(request, 'users/register.html', {'form':form})
