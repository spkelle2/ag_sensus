from __future__ import unicode_literals

from django.db import models

# Create your models here.


# variable names are also Database column names
# field defines the type
# pass in human name in quotes otherwise use machine name
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


# foreign key relates Choice to a single Question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# the above creates a database schema
# and Python database-access API for accessing Question/Choice objects

