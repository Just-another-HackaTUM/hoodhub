from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from .forms import CreateMessageForm, CreateChatForm, GetMessagesForm
from offers.models import Chat

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

@login_required
def create_chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'})

    form = CreateChatForm(request.POST)

    if not form.is_valid():
        return JsonResponse({'error': form.errors})

    chat = form.create_chat(request.user)

    return JsonResponse(chat, safe=False)


@login_required
def get_messages(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method'})

    form = GetMessagesForm(request.GET)

    if not form.is_valid():
        return JsonResponse({'error': form.errors})

    messages = form.get_messages(request.user)

    return JsonResponse(messages, safe=False)






