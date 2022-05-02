from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import *

#
# class CategoryListView(ListView):
#     model = Clients
#     template_name = 'index.html'
#     context_object_name = 'category'
#     paginate_by = 20

#
# def partners(request):
#     return render(request, "partners.html")


def home(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'home.html', context)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['recommendation'] = News.objects.all().order_by('-date')[:6]
    #     return context