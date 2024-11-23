from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .models import Offer
from .forms import (
    CreateOfferForm,
    UpdateOfferForm,
    SearchOfferForm,
    UUIDOfferForm,
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    form = CreateOfferForm(request.POST)

    if form.is_valid() and form.create(request.user):
        return HttpResponse("Offer created successfully", status=200)
    return HttpResponse("Offer creation failed", status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update(request):
    form = UpdateOfferForm(request.POST)

    if form.is_valid() and form.update(request.user):
        return HttpResponse("Offer updated successfully")
    return HttpResponse("Offer update failed", status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def search(request):
    form = SearchOfferForm(request.POST)

    if not form.is_valid():
        return JsonResponse({"error": form.errors})

    offers = form.search()
    return JsonResponse(offers, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_offer(request):
    form = UUIDOfferForm(request.GET)

    if not form.is_valid():
        return JsonResponse({"error": form.errors})

    offer = form.get_offer()
    return JsonResponse(offer, safe=False)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def react(request):
    form = UUIDOfferForm(request.PUT)

    if not form.is_valid():
        HttpResponse("Reaction failed: Form invalid", status=400)

    if not form.react():
        return HttpResponse(
            "Reaction failed: Offer does not exist", status=400
        )

    return HttpResponse("Reaction successful", status=200)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def deactivate(request):
    form = UUIDOfferForm(request.PUT)

    if not form.is_valid():
        HttpResponse("Deactivation failed: Invalid form", status=400)

    if not form.deactivate(request.user):
        return HttpResponse(
            "Deactivation failed: Offer does not exist", status=400
        )

    return HttpResponse("Deactivation successful", status=200)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def activate(request):
    form = UUIDOfferForm(request.PUT)

    if not form.is_valid():
        HttpResponse("Activation failed: Form is invalid", status=400)

    if not form.activate(request.user):
        return HttpResponse(
            "Activation failed: Offer does not exist", status=400
        )

    return HttpResponse("Activation successful", status=200)


def get_offers_of_user(request, user_id):
    return Offer.get_offers_of_user(user_id)
