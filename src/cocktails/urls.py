from django.urls import path
from . import views


urlpatterns = [
    path("",views.cocktailsView.as_view(), name="cocktails")
]




