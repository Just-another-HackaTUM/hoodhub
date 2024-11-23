from typing import Any
from django import forms
from django.core.exceptions import ValidationError

from backend.offers.models import Chat, Message


class CreateMessageForm(forms.Form):
    chat = forms.UUIDField()
    author = forms.UUIDField()

    content = forms.CharField(max_length=255)

    created_at = forms.DateTimeField(auto_now_add=True)

    def create_msg(self, author):
        content = self.cleaned_data['content']
        chat = Chat.objects.get(identifier=self.cleaned_data['chat'])

        return Message.objects.create(chat=chat, author=author, content=content)

class CreateChatForm(forms.Form):
    offer = forms.UUIDField()
    author = forms.UUIDField()

    def create_chat(self, author):
        offer = self.cleaned_data['offer']

        return Chat.objects.create(author=author, offer=offer)

class GetMessagesForm(forms.Form):
    chat = forms.UUIDField()

    def get_messages(self, user):
        chat = Chat.objects.get(identifier=self.cleaned_data['identifier'])

        if user != chat.author and user != chat.offer.author:
            raise PermissionError('You are not permitted to read this chat.')

        return Chat.get_messages(chat_id=chat)