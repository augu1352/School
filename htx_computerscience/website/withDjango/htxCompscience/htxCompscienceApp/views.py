from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    form = TestForm()

    return render(request, "index.html", {"form": form})
