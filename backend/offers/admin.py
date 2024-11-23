from django.contrib import admin

from .models import Topic, Offer, Chat, Message

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'created_at')
    search_fields = ('name', 'color')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'location', 'topic', 'created_at')
    search_fields = ('title', 'author__username', 'location', 'topic__name')
    list_filter = ('topic', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('offer', 'author', 'created_at')
    search_fields = ('offer__title', 'author__username')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('offer', 'author')
