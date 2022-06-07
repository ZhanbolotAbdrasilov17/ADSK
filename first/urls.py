from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('employee', employee, name='employee'),
    path('news', news, name='news'),
    path('news/<int:news_id>/', NewsDetail.as_view(), name='news'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
