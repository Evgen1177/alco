
from django.views.generic import ListView

from beer.models import Beer


class beerView(ListView):
    template_name = "beer/index.html"
    model = Beer
