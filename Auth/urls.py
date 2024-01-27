from django.urls import path
from . import views


urlpatterns =[
    path('', views.entry, name='entry'),
    path('signin/',views.SignInView.as_view(),name="Auth.signin"),
    path('signup/', views.SignUpView.as_view(), name='Auth.signup')
]