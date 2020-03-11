from django.contrib.auth.forms import UserCreationForm as UCF
from . import models

class UserCreationForm(UCF):
    class Meta(UCF.Meta):
        model = models.User
        fields = ("email","username","role",)
    
    def send_mail(self):
        # TODO
        # sending mail
        print("Sending Mail")