from django.contrib import admin
from .models import Question,Test,GradedTest,TestQuestion,Theme,GradedTestquestion

# Register your models here.
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(GradedTest)
admin.site.register(TestQuestion)
admin.site.register(GradedTestquestion)
admin.site.register(Theme)