from django.views.generic import ListView
from django.shortcuts import render

from .models import *


class CategoryListView(ListView):
    model = Clients
    template_name = 'index.html'
    context_object_name = 'category'
    paginate_by = 20


def partners(request):
    return render(request, "partners.html")
