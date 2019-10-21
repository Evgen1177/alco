from pathlib import Path
from platform import system
# from typing import NamedTuple

from django.shortcuts import render

from home.models import Alco


#class Alco(NamedTuple):
  # color: str
   #url = []
   #description = ""
   # url = URLField()
  #  description = TextField()


def get_alco():
    img_dir = Path(__file__).parent / "static" / "home"
    images = img_dir.glob("*.jp*g")

    result = []

    for image in images:
        alco = Alco(url=f"static/home/{image.name}", description=f"Image {image.name}")
        result.append(alco)

    return result


def index(request):
    return render(request, "home/index.html", {
       #  "alcos": get_alco(),
        "alcos": Alco.objects.all(),
    })
