from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.


# variable names are also Database column names
# field defines the type
# pass in human name in quotes otherwise use machine name
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # have questions show up as their text and not object type
    def __str__(self):
        return self.question_text

    # custom method for returning questions made in last day
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# foreign key relates Choice to a single Question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # have choices show up as their text and not object type
    def __str__(self):
        return self.choice_text

# the above creates a database schema
# and Python database-access API for accessing Question/Choice objects

