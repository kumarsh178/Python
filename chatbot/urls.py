from django.urls import path
from .views import chat_page, chat_api, chat_api_with_ai, chat_with_ai_page

urlpatterns = [
    path("chatwithdb/", chat_page),
    path("chatwithaipage/", chat_with_ai_page),
    path("api/", chat_api),
    path("chatwithai/", chat_api_with_ai) # post mana or rest api
]