from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home.base'),
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)