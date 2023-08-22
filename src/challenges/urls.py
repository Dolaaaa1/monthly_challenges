from django.urls import path
from . import views

urlpatterns = [
    path("", views.indix,name="index"),
    path("<int:month>",views.manthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge,name="month-challenge"),
]
