from django.urls import path
from . import views

app_name = 'Portfolio'

urlpatterns = [
    path('upload/', views.portfolio_create, name='create')
]