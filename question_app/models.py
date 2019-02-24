from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    answer = models.TextField(max_length=150)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    use_rate = models.IntegerField()
    def __str__(self):
        return self.question_text