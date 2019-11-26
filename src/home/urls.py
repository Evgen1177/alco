from django.urls import path

from . import views

urlpatterns = [
    path("", views.AlcoView.as_view(), name='index'),
]