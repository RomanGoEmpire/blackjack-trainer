from django.urls import path

from . import views

app_name = "blackjack"
urlpatterns = [
    path("", views.index, name="index"),
    path("cards/", views.cards, name="cards"),
    path("tables/", views.tables, name="tables"),
]
