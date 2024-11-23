from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("update", views.update, name="update"),
    path("get_offer", views.get_offer, name="get_offer"),
    path("search", views.search, name="search"),
    path("react", views.react, name="react"),
    path("deactivate", views.deactivate, name="deactivate"),
    path("activate", views.activate, name="activate"),
    path(
        "get_offers_of_user/<uuid:offer_id>",
        views.get_offers_of_user,
        name="get_offers_of_user",
    ),
]
