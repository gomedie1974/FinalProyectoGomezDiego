# mensajeria/urls.py
from django.urls import path
from .views import chat_list, chat_detail

urlpatterns = [
    path('chats/', chat_list, name='chat_list'),
    path('chat/<int:chat_id>/', chat_detail, name='chat_detail'),

    
]
