from django.urls import path

from . import views

urlpatterns = [
    # -------- Chat -----------------
    path('create_msg', views.create_msg, name='create_msg'),
    path('create_chat', views.create_chat, name='create_chat'),
    path('get_messages', views.get_messages, name='get_messages')
]
