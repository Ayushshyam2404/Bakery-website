from django.urls import path
from django.views import generic
from django.views.generic.base import TemplateView
from . import views
app_name='baker'
urlpatterns=[
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name="add"),
    path('view/', views.viewer, name="viewer"),
    path('update_item/', views.update_item, name="update_item"),
    path('delete_item', views.delete_item, name="delete_item"),
    path('orders/', views.orders, name="orders"),
    path('profile/', views.profile, name='profile')
]