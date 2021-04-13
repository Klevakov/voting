from django.contrib import admin

from .models import Person, Vote, VoteToPerson


# class PersonInline(admin.StackedInline):
#     model = Person
#     extra = 1


# class VoteToPersonInline(admin.StackedInline):
#     model = VoteToPerson
#     extra = 1


class VoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['voting_name', 'voting_description']}),
        ('Период голосования', {'fields': ['start_date', 'end_date']}),
        ('Информация о победителе', {'fields': ['number_of_votes_for_win', 'winner']}),
    ]
    list_display = ('voting_name', 'start_date', 'end_date', 'winner')
    list_filter = ['start_date']
    search_fields = ['voting_name']
    # inlines = [PersonInline]
    # inlines = [VoteToPersonInline]


class PersonAdmin(admin.ModelAdmin):
    fields = ['surname', 'name', 'middle_name',
              'photo', 'age', 'short_biography']
    list_display = ('name', 'middle_name', 'age')


class VoteToPersonAdmin(admin.ModelAdmin):
    fields = ['vote', 'person']
    list_display = ('vote', 'person', 'number_of_votes')


admin.site.register(Vote, VoteAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(VoteToPerson, VoteToPersonAdmin)


