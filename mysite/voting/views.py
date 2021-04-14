from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Max

from datetime import datetime, date

from .models import Person, Vote


def index(request):
    latest_votes_list = Vote.objects.order_by('-id')[:10]
    context = {
        'latest_votes_list': latest_votes_list,
    }
    return render(request, 'voting/index.html', context)


def detail(request, vote_id):
    my_vote = get_object_or_404(Vote, pk=vote_id)
    if my_vote.start_date < date.today() <= my_vote.end_date:
        if my_vote.winner == 'Победитель пока не определен. Голосование продолжается.':
            my_person_list = my_vote.person.all()
            context = {
                'vote': my_vote,
                'person_list': my_person_list,
            }
            return render(request, 'voting/detail.html', context)
        else:
            return HttpResponseRedirect(reverse('voting:results', args=(my_vote.id,)))
    else:
        return determine_the_winner_two(vote=my_vote)


def results(request, vote_id):
    my_vote = get_object_or_404(Vote, pk=vote_id)
    my_person_list = my_vote.vote_to_person.all()

    context = {
        'vote': my_vote,
        'person_list': my_person_list,
        'winner': my_vote.winner
    }
    return render(request, 'voting/results.html', context)


def voice(request, vote_id):
    my_vote = get_object_or_404(Vote, pk=vote_id)
    try:
        person_id = request.POST['person']
    except KeyError:
        my_person_list = my_vote.person.all()
        context = {
            'vote': my_vote,
            'person_list': my_person_list,
            'error_message': "Вы не сделали выбор.",
        }
        return render(request, 'voting/detail.html', context)
    else:
        selected_vote = my_vote.vote_to_person.select_for_update().filter(vote=my_vote.id)
        with transaction.atomic():
            if my_vote.winner == 'Победитель пока не определен. Голосование продолжается.':
                selected_person = selected_vote.get(person=person_id)
                selected_person.number_of_votes = F('number_of_votes') + 1
                selected_person.moment_of_last_voice = datetime.now()
                selected_person.save()
                selected_person.refresh_from_db()
                if my_vote.number_of_votes_for_win is not None:
                    determine_the_winner_one(vote=my_vote, person=selected_person)

        return HttpResponseRedirect(reverse('voting:results', args=(my_vote.id,)))


def determine_the_winner_one(vote: Vote, person: Person) -> None:
    """Если счетчик персонажа достиг количества голосов, достаточных для досрочного завершения голосования',
    функция подсчитывает победителя и записывает результат в БД"""

    if person.number_of_votes == vote.number_of_votes_for_win:
        vote.winner = 'Голосование завершено досрочно. Победитель - ' + str(person.person)
        vote.save()
        vote.refresh_from_db()
    return HttpResponseRedirect(reverse('voting:results', args=(vote.id,)))


def determine_the_winner_two(vote: Vote) -> None:
    if vote.winner == 'Победитель пока не определен. Голосование продолжается.':
        selected_vote = vote.vote_to_person.aggregate(Max('number_of_votes'))
        winners = vote.vote_to_person.filter(number_of_votes=selected_vote['number_of_votes__max'])
        if winners.count() > 1:
            current_winner = None
            for winner in winners:
                if current_winner is None:
                    current_winner = winner
                if winner.moment_of_last_voice < current_winner.moment_of_last_voice:
                    current_winner = winner
            vote.winner = 'Период голосования закончился. Победитель  - ' + str(current_winner.person) + \
                          ' ранее остальных набрал максимальное количество голосов.'
        else:
            current_winner = winners[0]
            vote.winner = 'Период голосования закончился. Победитель  - ' + str(current_winner.person)
        vote.save()
        vote.refresh_from_db()
    return HttpResponseRedirect(reverse('voting:results', args=(vote.id,)))

