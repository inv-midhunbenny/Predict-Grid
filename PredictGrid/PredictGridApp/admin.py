from django.contrib import admin
from PredictGridApp.models import Groups,User,UserAnswer,Question,Option
# Register your models here.
admin.site.register(Groups)
admin.site.register(Option)
admin.site.register(UserAnswer)
admin.site.register(User)
admin.site.register(Question)
