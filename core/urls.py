from django.urls import path, include
from .views import DifferenceView

urlpatterns = [

    path('difference/', DifferenceView.as_view(), name='difference'),
]