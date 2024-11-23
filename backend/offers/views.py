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

def offers(request):
    return HttpResponse("Hello, world. You're at the index.")