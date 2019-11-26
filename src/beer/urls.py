from django.urls import path
from . import views


urlpatterns = [
    path("",views.beerView.as_view(), name="beer")
]







