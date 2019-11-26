from django.views.generic import ListView

from whiskey.models import Whiskey


class whiskeyView(ListView):
    template_name = "whiskey/index.html"
    model = Whiskey



