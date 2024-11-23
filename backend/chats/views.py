from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from backend.chats.forms import CreateMessageForm
from backend.offers.models import Chat

# Create your views here.
@login_required
def create_msg(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'})

    form = CreateMessageForm(request.POST)

    if not form.is_valid():
        return JsonResponse({'error': form.errors})

    message = form.create_msg(request.user)

    return JsonResponse(message, safe=False)





