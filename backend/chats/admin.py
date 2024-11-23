from django.contrib import admin

from backend.offers.models import Chat


# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('offer', 'author', 'created_at')
    search_fields = ('offer__title', 'author__username')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('offer', 'author')
