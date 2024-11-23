from uuid import uuid4

from django.db import models


class Topic(models.Model):
    identifier = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)


class Offer(models.Model):
    identifier = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    reaction = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    participants = models.ManyToManyField('auth.User', related_name='offers', blank=True)

    def get_active_offers(self):
        return self.objects.filter(active=True).order_by('-created_at')

    def is_active(self):
        return self.active


class Chat(models.Model):
    identifier = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    identifier = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
