from django.urls import path


from .views import *

urlpatterns = [
    # path('', CategoryListView.as_view(), name="home"),
    path('', home, name='home'),
    path('news/<int:news_id>/', NewsDetailView.as_view(), name='news'),
]
