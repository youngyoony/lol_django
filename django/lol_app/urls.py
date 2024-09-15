from django.urls import path
from . import views

urlpatterns = [
    path("top_player", views.fetch_all_top_players, name="fetch_all_top_players"),
    path("top_player/create", views.save_top_player, name="save_top_player"),
    path("match/create", views.save_match, name="save_match"),
    path("match/detail/create", views.save_match_detail, name="save_match_detail"),
]