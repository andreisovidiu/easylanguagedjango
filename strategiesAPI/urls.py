from django.urls import path
from . import views

urlpatterns = [
    path('strategies/', views.strategies),
    path('strategies/<int:id>', views.single_strategy),
]