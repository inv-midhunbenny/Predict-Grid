# Generated by Django 4.0.3 on 2022-04-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PredictGridApp', '0008_question_date_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_question',
            field=models.DateField(),
        ),
    ]