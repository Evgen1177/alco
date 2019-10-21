from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("",TemplateView.as_view(template_name="cocktails/index.html"), name="cocktails")
]