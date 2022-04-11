from audioop import reverse
from email import message
from pickletools import optimize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator

from PredictGridApp.models import *
from PredictGridApp.forms import *

# Create your views here.

class Login(TemplateView):
    model = User
    form_class = LoginForm
    template_class = "PredictGridApp/login.html"
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
                print(obj1)
        else:
            message.error(request,"Invalid login")
            return redirect(reverse)

class Result(TemplateView):
    model = UserAnswer
    form_class = UserAnswerForm()
    template_class = 'result.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        self.context['question'] = Question.objects.all()
        self.context['option'] = Option.objects.all()
        self.context['result'] = self.form_class
        return render (request, self.template_class, self.context)
