# yourapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send-message/', views.send_message_view, name='send_message'),
]