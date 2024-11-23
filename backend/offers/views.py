from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from .models import Offer
from .forms import CreateOfferForm, UpdateOfferForm, SearchOfferForm, UUIDOfferForm
from .serializers import OfferSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


@login_required
def create(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method", status=405)

    form = CreateOfferForm(request.POST)

    if not form.is_valid():
        return HttpResponse("Offer creation failed", status=400)

    form.create(request.user)
    return HttpResponse("Offer created successfully", status=200)


@login_required
def update(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")

    form = UpdateOfferForm(request.POST)

    if not form.is_valid():
        return HttpResponse("Offer update failed")

    form.update(request.user)
    return HttpResponse("Offer updated successfully")



@login_required
def search(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'})

    form = SearchOfferForm(request.POST)

    if not form.is_valid():
        return JsonResponse({'error': form.errors})

    offers = form.search()
    return JsonResponse(offers, safe=False)


@login_required
def get_offer(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method'})

    form = UUIDOfferForm(request.GET)

    if not form.is_valid():
        return JsonResponse({'error': form.errors})

    offer = form.get_offer()
    return JsonResponse(offer, safe=False)


@login_required
def react(request):
    if request.method != 'PUT':
        return HttpResponse("Invalid request method", status=405)

    form = UUIDOfferForm(request.PUT)

    if not form.is_valid():
        HttpResponse("Reaction failed: Form invalid", status=400)

    if not form.react():
        return HttpResponse("Reaction failed: Offer does not exist", status=400)

    return HttpResponse("Reaction successful", status=200)

@login_required
def deactivate(request):
    if request.method != 'PUT':
        return HttpResponse("Invalid request method", status=405)

    form = UUIDOfferForm(request.PUT)

    if not form.is_valid():
        HttpResponse("Deactivation failed: Invalid form", status=400)

    if not form.deactivate():
        return HttpResponse("Deactivation failed: Offer does not exist", status=400)

    return HttpResponse("Deactivation successful", status=200)


@login_required
def activate(request):
    if request.method != 'PUT':
        return HttpResponse("Invalid request method", status=405)

    form = UUIDOfferForm(request.PUT)

    if not form.is_valid():
        HttpResponse("Activation failed: Form is invalid", status=400)

    if not form.activate():
        return HttpResponse("Activation failed: Offer does not exist", status=400)

    return HttpResponse("Activation successful", status=200)

def get_offers_of_user(request, user_id):
    return Offer.get_offers_of_user(user_id)
