from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Offer

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

'''
def offers(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello, world!'})
    else:
        return JsonResponse({'message': 'Hello, world!'})return HttpResponse("Hello, world. You're at the polls index.")
'''

# /offers/test endpoints
def offers(request):
    if request.method == 'GET':
        mock_offers = [
            {"id": 1, "title": "Offer 1", "description": "Description for offer 1"},
            {"id": 2, "title": "Offer 2", "description": "Description for offer 2"},
            {"id": 3, "title": "Offer 3", "description": "Description for offer 3"}
        ]

        return JsonResponse(mock_offers, safe=False)

    return JsonResponse({'message': 'Invalid request method'}, status=405)