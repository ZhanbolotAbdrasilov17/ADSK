from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.conf import settings

from .models import *


def appeal(request):
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        msg = f'Subject {data["subject"]} \n Name {data["name"]}\n' \
              f' Message {data["message"]} \n Email {email}'
        send_mail('Образец', msg, settings.EMAIL_HOST_USER, ['zhanbolot19971997@gmail.com'])
    return HttpResponseRedirect(redirect_to=reverse('home'))


def home(request):
    employees = Employee.objects.all()
    news_ = News.objects.all()
    context = {"employees": employees, "news": news_, 'last_four_news': news_.order_by('created_at')[:4],
               'token': get_token(request)}
    return render(request, "home.html", context)


def employee(request):
    employee_ = Employee.objects.all()
    context = {"employee": employee_}
    return render(request, "team.html", context)


class EmployeeDetail(DetailView):
    model = Employee
    template_name = "team-detail.html"
    context_object_name = 'employees'
    pk_url_kwarg = 'employees_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = Emdescription.objects.all()
        return context


def news(request):
    newses = News.objects.all()
    context = {"news": newses, 'last_four_news': newses.order_by('created_at')[:4]}
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