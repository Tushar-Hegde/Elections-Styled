from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from questionnaire.models import Surveys
import json
import users

# Create your views here.

def home(request):
    requiredQuestions={}
    s_id = users.views.s_id
    print(s_id)
    surveyInfo = Surveys.objects.get(id=s_id)
    questions = json.loads(surveyInfo.questions)
    requiredQuestions.update(questions)
    return render(request, 'ElectionCode/homepage.html', {'pageName':'Voting Page', 'requiredQuestions':requiredQuestions})

def live(request):
    return render(request, 'ElectionCode/live.html', {'pageName':'Live Poll'})
    
