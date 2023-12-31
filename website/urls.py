from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
]