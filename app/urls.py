from importlib.resources import path
from django.urls import path
from app import views

urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('datail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about'),
]