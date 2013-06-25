from django.http import HttpResponse
from django.view.generic import ListView

class StatsList(ListView):
    model = Stats
