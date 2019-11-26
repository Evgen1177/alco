from django.urls import path
from . import views


urlpatterns = [
    path("",views.whiskeyView.as_view(), name="whiskey")


]







