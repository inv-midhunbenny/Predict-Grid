from django import forms
from django.forms import ModelForm
from PredictGridApp.models import Groups,UserAnswer,User,Option,Question
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget= forms.PasswordInput())

    
class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = [
            'user_id',
            'question_id',
            'option1',
            'option2',
            'option3',
            'option4',
            
        ]