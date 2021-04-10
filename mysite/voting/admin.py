from django.contrib import admin

from .models import Person, Vote, VoteToPerson

admin.site.register(Person)
admin.site.register(Vote)
admin.site.register(VoteToPerson)
