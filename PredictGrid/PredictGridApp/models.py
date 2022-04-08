from email.policy import default
from tokenize import group
from django.db import models

# Create your models here.
class Groups(models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=50)
    points=models.IntegerField(null=False,default=0)
    created_at=models.DateField(null=False)
    updated_at=models.DateField(null=False)

    class Meta:
        db_table="group"

class Users(models.Model):
    uid=models.IntegerField(primary_key=True)
    group_id=models.ForeignKey(Groups,on_delete=models.CASCADE)
    name=models.CharField(null=False,max_length=50)
    email=models.EmailField(null=False)
    password=models.CharField(null=False,default='Inn0v@tur3',max_length=16)
    points=models.IntegerField(null=False,default=0)
    status=models.BooleanField(null=False)
    created_at=models.DateField(null=False)
    updated_at=models.DateField(null=False)

    class Meta:
        db_table="users"


class Question(models.Model):
    uid=models.AutoField(primary_key=True)
    question=models.CharField(null=False,max_length=100)
    created_at=models.DateField(null=False)
    updated_at=models.DateField(null=False)

    class Meta:
        db_table="question"

class Option(models.Model):
    uid=models.AutoField(primary_key=True)
    questionid=models.ForeignKey(Question,on_delete=models.CASCADE)
    option1=models.CharField(null=False,max_length=200)
    option2=models.CharField(null=False,max_length=200)
    option3=models.CharField(null=False,max_length=200)
    option4=models.CharField(null=False,max_length=200)
    status=models.BooleanField(null=False)
    created_at=models.DateField(null=False)
    updated_at=models.DateField(null=False)

    class Meta:
        db_table="option"

class UserAnswer(models.Model):
    uid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(Users,on_delete=models.CASCADE)
    questionid=models.ForeignKey(Question,on_delete=models.CASCADE)
    option1=models.CharField(null=False,default=0,max_length=200)
    option2=models.CharField(null=False,default=0,max_length=200)
    option3=models.CharField(null=False,default=0,max_length=200)
    option4=models.CharField(null=False,default=0,max_length=200)
    created_at=models.DateField(null=False)
    updated_at=models.DateField(null=False)

    class Meta:
        db_table="user_answer"



            






