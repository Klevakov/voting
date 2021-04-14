from django.urls import path

from . import views

app_name = 'voting'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vote_id>/', views.detail, name='detail'),
    path('<int:vote_id>/results/', views.results, name='results'),
    path('<int:vote_id>/voice/', views.voice, name='voice'),
]