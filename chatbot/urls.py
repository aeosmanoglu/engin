from django.urls import path

from .views import chat_view, new_chat

urlpatterns = [
    path('', chat_view, name='chat_view'),
    path('new_chat/', new_chat, name='new_chat'),
]
