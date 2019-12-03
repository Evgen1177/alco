from django import forms
from django.views.generic import ListView
from django.db.models import Q

from beer.models import Beer
from cocktails.models import Cocktails
from home.models import Alco
from whiskey.models import Whiskey


class SearchForm(forms.Form):
    search = forms.CharField()


class AlcoView(ListView):
    template_name = "home/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx["search_form"] = SearchForm()
        return ctx

    def get_queryset(self, name__icontains=None):
        f = SearchForm(self.request.GET)

        result = []

        for model in (Whiskey, Beer, Cocktails):
            future_alcos = model.objects.all()
            if f.is_valid():
                future_alcos = future_alcos.filter(name__istartswith =f.data["search"])
               #future_alcos = future_alcos.filter(name__icontains == f.data["search"])
               # future_alcos = future_alcos.filter(name=f.data["search"])
                #future_alcos = future_alcos.filter(Q(name=f.data["search"]) | Q(name__icontains=query))
            for obj in future_alcos:
                result.append(obj)

        return result
