from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView, SignInView, SignOutView
from . import views




urlpatterns = [
    path('', views.entry, name='entry'),
    path('accounts/profile/', views.HomeView.as_view(), name='home.base'),

    ####login####
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    #path('signout/', SignOutView.as_view(), name='signout'),
    #path('accounts/profile/', AuthorizedView.as_view(), name='accounts/profile/'),
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)