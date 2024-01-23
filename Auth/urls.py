from django.urls import path
from . import views


urlpatterns =[
    path('', views.Homepage, name='Auth.base'),
    path('authorised/', views.AuthorizedView.as_view()),
    path('signin/',views.SignInView.as_view(),name="Auth.signin"),
    path('signout/',views.SignOutView.as_view(),name="Auth.signout"),
    path('signup/', views.SignUpView.as_view(), name='Auth.signup')
]