from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from backend.offers.models import Chat, Message, Offer


class CreateMessageForm(forms.Form):
    chat = forms.UUIDField()
    author = forms.UUIDField()
    content = forms.CharField(max_length=255)
    created_at = forms.DateTimeField(auto_now_add=True)

    def validate_chat(self):
        try:
            Chat.objects.get(identifier=self.cleaned_data['chat'])
        except Chat.DoesNotExist:
            raise forms.ValidationError('Invalid chat.')

    def validate_author(self):
        try:
            User.objects.get(identifier=self.cleaned_data['author'])
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid author.')

    def create_msg(self, author):
        content = self.cleaned_data['content']
        chat = Chat.objects.get(identifier=self.cleaned_data['chat'])

        if chat.author != author and chat.offer.author != author:
            raise PermissionError('You are not permitted to write to this chat')

        return Message.objects.create(chat=chat.identifier, author=author, content=content)

class CreateChatForm(forms.Form):
    offer = forms.UUIDField()

    def validate_offer(self):
        try:
            Offer.objects.get(identifier=self.cleaned_data['offer'])
        except Offer.DoesNotExist:
            raise forms.ValidationError('Invalid offer.')

    def create_chat(self, author):
        offer = self.cleaned_data['offer']
        return Chat.objects.create(author=author, offer=offer)

class GetMessagesForm(forms.Form):
    chat = forms.UUIDField()

    def validate_chat(self):
        try:
            Chat.objects.get(identifier=self.cleaned_data['chat'])
        except Chat.DoesNotExist:
            raise forms.ValidationError('Invalid chat.')

    def get_messages(self, user):
        chat = Chat.objects.get(identifier=self.cleaned_data['chat'])

        if user != chat.author and user != chat.offer.author:
            raise PermissionError('You are not permitted to read this chat.')

        return Chat.get_messages(chat_id=chat)