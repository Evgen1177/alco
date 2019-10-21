from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("",TemplateView.as_view(template_name="beer/index.html"), name="beer")
]