from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views




urlpatterns = [

    path('home/', views.HomeView.as_view(), name='home.base'),
    path('homedata/', views.HomeData.as_view(), name='homedata.base'),


    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)