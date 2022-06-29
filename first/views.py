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
    employees = Sotrudniki.objects.all()
    news_ = Novosti.objects.all()
    partners = Partners.objects.all()
    quotes = Tchitaty.objects.all()
    quotes_managers = TchitatyMenedzherov.objects.all()
    video_content = VideoContent.objects.all()
    results = RezultatyOblastey.objects.all()
    oblast1 = RezultatyOblastey.objects.get(id=1)
    oblast2 = RezultatyOblastey.objects.get(id=2)
    oblast3 = RezultatyOblastey.objects.get(id=3)
    oblast4 = RezultatyOblastey.objects.get(id=4)
    oblast5 = RezultatyOblastey.objects.get(id=5)
    oblast6 = RezultatyOblastey.objects.get(id=6)
    oblast7 = RezultatyOblastey.objects.get(id=7)
    oblast8 = RezultatyOblastey.objects.get(id=8)
    projects = Proekty.objects.all()
    portfolio_ = Portfolio.objects.all()
    context = {"employees": employees, "news": news_, 'last_four_news': news_.order_by('created_at')[:4],
               'token': get_token(request), "partners": partners, "quotes": quotes,
               "quotes_managers": quotes_managers, "video_content": video_content, "results": results,
               'oblast1': oblast1, 'oblast2': oblast2, 'oblast3': oblast3,
               'oblast4': oblast4, 'oblast5': oblast5, 'oblast6': oblast6,
               'oblast7': oblast7, 'oblast8': oblast8, 'projects': projects, 'portfolio_': portfolio_,
               }
    return render(request, "home.html", context)


def our_companies(request):
    portfolios = PortFolioCompanies.objects.all()
    context = {"portfolios": portfolios, }
    return render(request, "our_companies.html", context)


def portfolio(request):
    projects = Proekty.objects.all()
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
        _news = Novosti.search_news(query)
    if not _news or query is None:
        _news = Novosti.objects.all()
    return render(request, "blog.html", {'news': _news, 'last_four_news': Novosti.last_four_news()})


# def get(self, request, *args, **kwargs):
#     self.object = self.get_object()
#     context = self.get_context_data(object=self.object)
#     return self.render_to_response(context)


def employee(request):
    employee_ = Sotrudniki.objects.all()
    congresses = MezhdunarodnyeKon.objects.all()
    quotes = TchitatyMenedzherov.objects.all()
    oblast1 = RezultatyOblastey.objects.get(id=1)
    oblast2 = RezultatyOblastey.objects.get(id=2)
    oblast3 = RezultatyOblastey.objects.get(id=3)
    oblast4 = RezultatyOblastey.objects.get(id=4)
    oblast5 = RezultatyOblastey.objects.get(id=5)
    oblast6 = RezultatyOblastey.objects.get(id=6)
    oblast7 = RezultatyOblastey.objects.get(id=7)
    oblast8 = RezultatyOblastey.objects.get(id=8)


    context = {"employee": employee_, "congresses": congresses, "quotes": quotes,
               'oblast1': oblast1, 'oblast2': oblast2, 'oblast3': oblast3,
               'oblast4': oblast4, 'oblast5': oblast5, 'oblast6': oblast6,
               'oblast7': oblast7, 'oblast8': oblast8}
    return render(request, "about.html", context)


class EmployeeDetail(DetailView):
    model = Sotrudniki
    template_name = "team-detail.html"
    context_object_name = 'employees'
    pk_url_kwarg = 'employees_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = EmDescription.objects.all()
        return context


def news(request):
    newses = Novosti.objects.all()
    new_techno = NovyeTehnologii.objects.all()
    media_news = Smi.objects.all()
    context = {"news": newses, 'last_four_news': Novosti.last_four_news(), "new_techno": new_techno, "media_news": media_news}
    return render(request, "blog.html", context)


class NewsDetail(DetailView):
    model = Novosti
    template_name = "blog-details.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['texts'] = FullDescription.objects.all()
        context['news_images'] = KartinkiNovostey.objects.all()
        return context





