from django.views.generic import ListView

from .models import *

class CategoryListView(ListView):
    model = Clients
    template_name = 'index.html'
    context_object_name = 'category'
    paginate_by = 20