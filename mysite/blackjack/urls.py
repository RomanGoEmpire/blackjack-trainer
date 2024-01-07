from django.urls import path

from . import views

app_name = "blackjack"
urlpatterns = [
    path("", views.index, name="home"),
    path("games/", views.games, name="games"),
    path("games/practice/", views.practice, name="practice"),
    path("tables/", views.tables, name="tables"),
    path("stats/", views.stats, name="stats"),
    path("selected/<str:option>/<str:mode>/", views.selected, name="selected"),
]
