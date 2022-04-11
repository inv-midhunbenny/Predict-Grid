from email.policy import default
from enum import auto
from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class Groups(models.Model):
    name=models.CharField(null=False,max_length=50)
    points=models.IntegerField(null=False,default=0)
    created_at=models.DateField(auto_now_add=True,null=False)
    updated_at=models.DateField(auto_now=True,null=False)

    class Meta:
        db_table="group"

class User(AbstractUser):
    group_id=models.ForeignKey(Groups,on_delete=models.CASCADE,default=1)
    name=models.CharField(null=False,max_length=50)
    email=models.EmailField(null=False)
    password=models.CharField(null=False,default='Inn0v@tur3',max_length=16)
    points=models.IntegerField(null=False,default=0)
    status=models.BooleanField(blank=True,null=True)
    created_at=models.DateField(auto_now_add=True,null=False)
    updated_at=models.DateField(auto_now=True,null=False)

    class Meta:
        db_table="users"


class Question(models.Model):
    question=models.CharField(null=False,max_length=100)
    created_at=models.DateField(auto_now_add=True,null=False)
    updated_at=models.DateField(auto_now=True,null=False)
    date_question=models.DateField(null=False)

    class Meta:
        db_table="question"

class Option(models.Model):
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE,default=0)
    option1=models.CharField(null=False,max_length=200)
    option2=models.CharField(null=False,max_length=200)
    option3=models.CharField(null=False,max_length=200)
    option4=models.CharField(null=False,max_length=200)
    status=models.BooleanField(null=False)
    created_at=models.DateField(auto_now_add=True,null=False)
    updated_at=models.DateField(auto_now=True,null=False)

    class Meta:
        db_table="option"

class UserAnswer(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE,default=0)
    option1=models.CharField(null=False,default=0,max_length=200)
    option2=models.CharField(null=False,default=0,max_length=200)
    option3=models.CharField(null=False,default=0,max_length=200)
    option4=models.CharField(null=False,default=0,max_length=200)
    created_at=models.DateField(auto_now_add=True,null=False)
    updated_at=models.DateField(auto_now=True,null=False)

    class Meta:
        db_table="user_answer"



            






