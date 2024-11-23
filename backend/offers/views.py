from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from .models import Offer
from .forms import CreateOfferForm, UpdateOfferForm, SearchOfferForm
from .serializers import OfferSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

@login_required
def create(request):
    if request.method == 'POST':
        form = CreateOfferForm(request.POST)

        if form.is_valid():
            form.create(request.user)
            return HttpResponse("Offer created successfully")
        else:
            return HttpResponse("Offer creation failed")
    else:
        return HttpResponse("Invalid request method")

@login_required
def update(request):
    if request.method == 'POST':
        form = UpdateOfferForm(request.POST)

        if form.is_valid():
            form.update(request.user)
            return HttpResponse("Offer updated successfully")
        else:
            return HttpResponse("Offer update failed")
    else:
        return HttpResponse("Invalid request method")

@login_required
def search(request):
    if request.method == 'POST':
        form = SearchOfferForm(request.POST)

        if form.is_valid():
            offers = form.search()
            return JsonResponse(offers, safe=False)

def get_offer(request, offer_id):
    return OfferSerializer(Offer.get_offer_with_id(offer_id)).data

def react(request, offer_id):
    Offer.add_reaction(offer_id)

def deactivate(request, offer_id):
    Offer.deactivate_offer(offer_id)

def activate(request, offer_id):
    Offer.activate_offer(offer_id)

def get_offers_of_user(request, user_id):
    return Offer.get_offers_of_user(user_id)

