from django.urls import path
from .views.competition_view import CompetitionsView, CompetitionView
from .views.competitors_view import CompetitorsView, CompetitorView
from  .views.referees_view import RefereesView, RefereeView

urlpatterns = [
    path('competitions/', CompetitionsView.as_view()),
    path('competition/<uuid:uuid>/', CompetitionView.as_view()),

    path('competitors/<uuid:competition_uuid>/', CompetitorsView.as_view()),
    path('competitor/<uuid:uuid>/', CompetitorView.as_view()),

    path('referees/<uuid:competition_uuid>/', RefereesView.as_view()),
    path('referee/<uuid:uuid>/', RefereeView.as_view())
]