from typing import Any
from django import forms
from django.core.exceptions import ValidationError

from backend.offers.models import Chat, Message


class CreateMessageForm(forms.Form):
    chat = forms.UUIDField()
    author = forms.UUIDField()

    content = forms.CharField(max_length=255)

    created_at = forms.DateTimeField(auto_now_add=True)

    def create_msg(self, author) -> bool:
        content = self.cleaned_data['content']
        chat = Chat.objects.get(identifier=self.cleaned_data['chat'])

        return Message.objects.create(chat=chat, author=author, content=content)