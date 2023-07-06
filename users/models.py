from django.db import models

# Create your models here.

class BasicInfo(models.Model):
    def __str__(self):
        return self.survey_name
    survey_id = models.CharField(max_length=200)
    survey_name = models.CharField(max_length=200)
    


        
