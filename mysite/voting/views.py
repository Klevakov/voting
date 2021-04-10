from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Vote, VoteToPerson


def index(request):
    latest_votes_list = Vote.objects.order_by('-start_date')[:2]
    output = ', '.join([v.voting_name for v in latest_votes_list])
    return HttpResponse(output)


def detail(request, vote_id):
    return HttpResponse(f"You're looking at vote %s." % vote_id)


def results(request, vote_id):
    response = "You're looking at the results of vote %s."
    return HttpResponse(response % vote_id)


def vote(request, vote_id):
    response = "You're voting on question %s."
    return HttpResponse(response % vote_id)
