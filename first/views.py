from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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
    partners = Partners.objects.all()
    quotes = Quotes.objects.all()
    context = {"employees": employees, "news": news_, 'last_four_news': news_.order_by('created_at')[:4],
               'token': get_token(request), "partners": partners, "quotes": quotes}
    return render(request, "home.html", context)


def our_companies(request):
    portfolios = PortFolioCompanies.objects.all()
    context = {"portfolios": portfolios, }
    return render(request, "our_companies.html", context)


def portfolio(request):
    projects = Projects.objects.all()
    portfolio_ = Portfolio.objects.all()
    context = {"projects": projects, "portfolio": portfolio_}
    return render(request, "portfolio.html", context)


class PortfolioDetail(DetailView):
    model = Portfolio
    template_name = "portfolio-detail.html"
    context_object_name = 'port'
    pk_url_kwarg = 'portfolio_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


def contact(request):
    return render(request, "contact.html")


@csrf_exempt
def search_news(request):
    query = request.GET.get('q')

    _news = None
    if query is not None:
        _news = News.search_news(query)
    if not _news or query is None:
        _news = News.objects.all()
    return render(request, "blog.html", {'news': _news, 'last_four_news': News.last_four_news()})


def employee(request):
    employee_ = Employee.objects.all()
    congresses = InternationalCongresses.objects.all()
    context = {"employee": employee_, "congresses": congresses}
    return render(request, "about.html", context)


class EmployeeDetail(DetailView):
    model = Employee
    template_name = "team-detail.html"
    context_object_name = 'employees'
    pk_url_kwarg = 'employees_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = EmDescription.objects.all()
        return context


def news(request):
    newses = News.objects.all()
    new_techno = NewTechno.objects.all()
    media_news = Media.objects.all()
    context = {"news": newses, 'last_four_news': News.last_four_news(), "new_techno": new_techno, "media_news": media_news}
    return render(request, "blog.html", context)


class NewsDetail(DetailView):
    model = News
    template_name = "blog-details.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = FullDescription.objects.all()
        return context



