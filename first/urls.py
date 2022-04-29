from django.urls import path

from . import views
from .views import CategoryListView, partners

urlpatterns = [
    path('', CategoryListView.as_view(), name="home"),
    path("partners/", views.partners, name="partners")
]
