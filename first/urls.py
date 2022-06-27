from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', employee, name='about'),
    path('our_companies', our_companies, name='our_companies'),
    path('employee/<int:employees_id>/', EmployeeDetail.as_view(), name='employee'),
    path('news', news, name='news'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),
    path('appeal/', appeal, name='appeal'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/<int:portfolio_id>/', PortfolioDetail.as_view(), name='portfolio'),
    path('contact/', contact, name='contact'),
    path('search', search_news, name='search'),


]
