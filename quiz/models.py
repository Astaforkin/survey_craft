from enum import unique
from django.db import models
from django.contrib.auth.models import User



class Poll(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    order = models.IntegerField(default=1)
    
    class Meta:
        unique_together = ('poll','text',)

    def __str__(self):
        return f'{self.text} ({self.poll.title})'
    

class AnswerOption(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        unique_together = ('question', 'text',)
    
    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_options = models.ForeignKey(AnswerOption, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('user', 'question',) 