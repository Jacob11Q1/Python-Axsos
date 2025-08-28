from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # root route to form
    path('result/', views.result, name='result'), # result route
]