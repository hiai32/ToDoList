from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    due = models.DateTimeField()
    priority = models.IntegerField()
    explanation = models.TextField()
    isAchieved = models.BooleanField(default=False)
    userId = models.IntegerField()
