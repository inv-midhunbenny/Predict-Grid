from audioop import reverse
from datetime import datetime
from email import message
from multiprocessing import context
from pickletools import optimize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator

from PredictGridApp.models import *
from PredictGridApp.forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()

# Create your views here.

def get_user_model():
    """
    Return the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )

class Login(TemplateView):
    model =User 
    form_class = LoginForm
    template_class = "login.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['login'] = self.form_class
        return render(request, self.template_class, self.context)
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        username = request.POST.get('username', False)
        password  = request.POST.get('password', False)

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            if user.is_authenticated:
                obj1 = User.objects.get(username=user)
                return redirect('ipl_result')
        else:
            message.error(request,"Invalid login")
            return redirect(reverse)

class Logout(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('login')



class Result(TemplateView):
    model = UserAnswer
    form_class = UserAnswerForm()
    template_class = 'polls.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        question =  Question.objects.filter(date_question = today).first()
        self.context['question'] = question
        option  =  Option.objects.filter(question_id = question).first()
        self.context['option'] = option
        self.context['result'] = self.form_class
        self.context['name']=request.user.username
        return render (request, self.template_class, self.context)

