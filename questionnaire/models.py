from django.db import models

class Surveys(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=50)
    questions = models.CharField(max_length=1000)