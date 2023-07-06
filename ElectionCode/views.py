from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from questionnaire.models import Surveys
import json
import users

# Create your views here.

def home(request):
    surveyInfo = Surveys.objects.all()
    requiredQuestions={}
    s_id = users.views.s_id
    print(s_id)
    for object in surveyInfo:
        if object.identity == s_id:
            questions = json.loads(object.questions)
            requiredQuestions.update(questions)
    return render(request, 'ElectionCode/homepage.html', {'pageName':'Voting Page', 'requiredQuestions':requiredQuestions})

def live(request):
    return render(request, 'ElectionCode/live.html', {'pageName':'Live Poll'})
    