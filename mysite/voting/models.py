from django.db import models


class Vote(models.Model):
    voting_name = models.CharField(max_length=20)
    voting_description = models.TextField()
    # start_date = models.DateField(auto_now=False, auto_now_add=False)



    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
