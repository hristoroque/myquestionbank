from django.db import models
from accounts.models import User
# Create your models here.
class Theme(models.Model):
    theme_name = models.CharField(max_length=50)
    theme_description = models.TextField(max_length=150)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    def __str__(self):
        return self.theme_name

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    answer = models.TextField(max_length=150)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    use_rate = models.IntegerField()
    themes = models.ManyToManyField(Theme)
    def __str__(self):
        return self.question_text

class Test(models.Model):
    test_name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.test_name #+ User.objects.get(pk = self.user_id).get_name()
        
class TestQuestion(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test,on_delete=models.CASCADE)
    score = models.IntegerField()

class GradedTest(models.Model):
    test_id = models.ForeignKey(Test,on_delete = models.CASCADE)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    grade = models.IntegerField()
    #def __str__():

class GradedTestquestion(models.Model):
    question_name = models.CharField(max_length = 50)
    test_id = models.ForeignKey(GradedTest,on_delete=models.CASCADE)
    user_answer = models.TextField(max_length=150)
    grade = models.IntegerField()
    #def __str__():


