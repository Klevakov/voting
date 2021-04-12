from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Person, Vote, VoteToPerson


# class IndexView(generic.ListView):
#     template_name = 'voting/index.html'
#     context_object_name = 'latest_voting_list'
#
#     def get_queryset(self):
#         """Return the last three published questions."""
#         return Vote.objects.order_by('-id')[:3]
#
#
# class DetailView(generic.DetailView):
#     model = Vote
#     template_name = 'voting/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Vote
#     template_name = 'voting/results.html'
#
#
# def voice(request, vote_id):
#     my_vote = get_object_or_404(Vote, pk=vote_id)
#     try:
#         selected_person = my_vote.person_set.get(pk=request.POST['person'])
#
#     except (KeyError, Person.DoesNotExist):
#         return render(request, 'voting/detail.html', {
#             'vote': my_vote,
#             'error_message': "Вы не сделали выбор.",
#         })
#     else:
#         # selected_person.votes += 1
#         selected_person.votes = F('votes') + 1
#         # selected_person.update(votes=F('votes') + 1)
#         selected_person.save()
#         selected_person.refresh_from_db()
#         return HttpResponseRedirect(reverse('voting:results', args=(my_vote.id,)))


def index(request):
    latest_votes_list = Vote.objects.order_by('-id')[:3]
    # template = loader.get_template('voting/index.html')
    context = {
        'latest_votes_list': latest_votes_list,
    }
    return render(request, 'voting/index.html', context)


# def detail(request, vote_id):
#     return HttpResponse(f"You're looking at vote %s." % vote_id)
# def detail(request, vote_id):
#     try:
#         votes = Vote.objects.get(pk=vote_id)
#     except Vote.DoesNotExist:
#         raise Http404("Такого голосования не существует")
#     # content = {'vote': votes}
#     return render(request, 'voting/detail.html', {'vote': votes})


def detail(request, vote_id):
    my_vote = get_object_or_404(Vote, pk=vote_id)
    # my_person = VoteToPerson.objects.filter(vote=my_vote)
    my_person_list = my_vote.person.all()
    context = {
        'vote': my_vote,
        'person_list': my_person_list,
    }
    return render(request, 'voting/detail.html', context)

#
# def results(request, vote_id):
#     response = "You're looking at the results of vote %s."
#     return HttpResponse(response % vote_id)


def results(request, vote_id):
    my_vote = get_object_or_404(Vote, pk=vote_id)
    my_person_list = my_vote.vote_to_person.all()

    context = {
        'vote': my_vote,
        'person_list': my_person_list,
    }
    return render(request, 'voting/results.html', context)


# def voice(request, vote_id):
#     response = "You're voting on question %s."
#     return HttpResponse(response % vote_id)


def voice(request, vote_id):
    my_vote = get_object_or_404(Vote, pk=vote_id)
    try:
        # selected_person = my_vote.person_set.get(pk=request.POST['person'])
        selected_person = my_vote.vote_to_person.get(person=request.POST['person'])

        # selected_person = my_vote.person.get(pk=request.POST['person'])
    except (KeyError, VoteToPerson.DoesNotExist):
        my_person_list = my_vote.person.all()
        context = {
            'vote': my_vote,
            'person_list': my_person_list,
            'error_message': "Вы не сделали выбор.",
        }
        return render(request, 'voting/detail.html', context)
    else:
        # selected_person.votes += 1
        selected_person.number_of_votes = F('number_of_votes') + 1
        # selected_person.update(votes=F('votes') + 1)
        selected_person.save()
        selected_person.refresh_from_db()
        return HttpResponseRedirect(reverse('voting:results', args=(my_vote.id,)))
