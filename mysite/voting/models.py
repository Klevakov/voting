from django.db import models


class VoteToPerson(models.Model):
    number_of_votes = models.IntegerField(default=0)


class Vote(models.Model):
    voting_name = models.CharField(max_length=20)
    voting_description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    number_of_votes_for_win = models.IntegerField(default=None)
    is_active = models.BooleanField(default=True)
    winner = models.CharField(max_length=20)
    vote_to_person = models.ForeignKey(VoteToPerson, on_delete=models.CASCADE)


class Person(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    photo = models.TextField()                   # - пропиши тут значение по умолчанию - путь к какой нибудь картинке
    age = models.IntegerField()
    short_biography = models.TextField()
    vote_to_person = models.ForeignKey(VoteToPerson, on_delete=models.CASCADE)








