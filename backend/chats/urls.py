from django.urls import path

from . import views

urlpatterns = [
    # -------- Chat -----------------
    path('create_msg', views.create_msg, name='create_msg'),

]
