from django.shortcuts import render
from django.views.generic import DetailView

from .models import *


def home(request):
    employees = Employee.objects.all()
    news = News.objects.all()
    context = {"employees": employees, "news": news}
    return render(request, "home.html", context)

def employee(request):
    employee = Employee.objects.all()
    context = {"employee": employee}
    return render(request, "team.html", context)

def news(request):
    newses = News.objects.all()
    context = {"news": newses}
    return render(request, "blog.html", context)


class NewsDetail(DetailView):
    model = News
    template_name = "blog-details.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = Fulldescription.objects.all()
        return context

# class CategoryListView(ListView):
#     model = Clients
#     template_name = 'index.html'
#     context_object_name = 'category'
#     paginate_by = 20

#
# def partners(request):
#     return render(request, "partners.html")

#
# def home(request):
#     news = News.objects.all()
#     context = {'news': news}
#     return render(request, 'index.html', context)
#
#
# class NewsDetailView(DetailView):
#     model = News
#     template_name = 'news.html'
#     context_object_name = 'news'
#     pk_url_kwarg = 'news_id'
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data()
#     #     context['recommendation'] = News.objects.all().order_by('-date')[:6]
#     #     return context