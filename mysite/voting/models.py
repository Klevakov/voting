from django.db import models
import datetime as dt


class Person(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    photo = models.TextField(default=r'mysite\voting\static\voting\IMG')  # - пропиши тут значение по умолчанию - путь к какой нибудь картинке
    age = models.IntegerField()
    short_biography = models.TextField()

    def __str__(self):
        return f'{self.name} {self.middle_name}'


class Vote(models.Model):
    voting_name = models.CharField(max_length=20)
    voting_description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=dt.date.today())
    end_date = models.DateField(auto_now=False, auto_now_add=False, default=dt.date.today() + dt.timedelta(days=5))
    number_of_votes_for_win = models.IntegerField(default=None)
    is_active = models.BooleanField(default=True)
    winner = models.CharField(max_length=40, default='Победитель пока не определен.')
    person = models.ManyToManyField(Person, through='VoteToPerson')

    def __str__(self):
        return self.voting_name


class VoteToPerson(models.Model):
    number_of_votes = models.IntegerField(default=0)
    vote = models.ForeignKey(Vote, default=0, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, default=0, on_delete=models.CASCADE)







