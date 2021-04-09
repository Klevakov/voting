from django.db import models


class Person(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    photo = models.TextField(default=r'mysite\voting\static\voting\IMG')  # - пропиши тут значение по умолчанию - путь к какой нибудь картинке
    age = models.IntegerField()
    short_biography = models.TextField()


class Vote(models.Model):
    voting_name = models.CharField(max_length=20)
    voting_description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    number_of_votes_for_win = models.IntegerField(default=None)
    is_active = models.BooleanField(default=True)
    winner = models.CharField(max_length=20)
    person = models.ManyToManyField(Person, through='VoteToPerson')


class VoteToPerson(models.Model):
    number_of_votes = models.IntegerField(default=0)
    vote = models.ForeignKey(Vote, default=0, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, default=0, on_delete=models.CASCADE)





