from django.urls import path
from core.views import predict

urlpatterns = [
    path('', predict, name="predict"),
]