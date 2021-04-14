from django.db import models
from django.utils import timezone
from datetime import datetime as dt


class Person(models.Model):
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    photo = models.TextField(default=r'\voting\static\voting\IMG')
    age = models.IntegerField()
    short_biography = models.TextField()

    def __str__(self):
        return f'{self.name} {self.middle_name}'


class Vote(models.Model):
    voting_name = models.CharField(max_length=40)
    voting_description = models.TextField()
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(default=timezone.now() + timezone.timedelta(days=3))
    number_of_votes_for_win = models.IntegerField(default=None)
    winner = models.CharField(max_length=150, default='Победитель пока не определен. Голосование продолжается.')
    person = models.ManyToManyField(Person, through='VoteToPerson')

    def __str__(self):
        return self.voting_name


class VoteToPerson(models.Model):
    number_of_votes = models.IntegerField(default=0)
    vote = models.ForeignKey(Vote, default=0, on_delete=models.CASCADE, related_name='vote_to_person')
    person = models.ForeignKey(Person, default=0, on_delete=models.CASCADE)
    moment_of_last_voice = models.DateTimeField(default=dt.now())
