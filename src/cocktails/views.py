
from django.views.generic import ListView

from cocktails.models import Cocktails


class cocktailsView(ListView):
    template_name = "cocktails/index.html"
    model = Cocktails



