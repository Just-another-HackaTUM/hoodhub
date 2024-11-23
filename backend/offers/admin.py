from django.contrib import admin
from django.contrib.auth.models import User

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Topic, Offer, Chat, Message


class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic
        import_id_fields = ('identifier',)


# Register your models here.
@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    resource_class = TopicResource
    
    list_display = ("name", "color", "created_at")
    search_fields = ("name", "color")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


class OfferResource(resources.ModelResource):
    class Meta:
        model = Offer
        import_id_fields = ('identifier',)

    def before_import_row(self, row, **kwargs):
        topic_identifier = row.get('topic')
        if topic_identifier:
            topic, _ = Topic.objects.get_or_create(identifier=topic_identifier)
            row['topic'] = topic.pk

        author_username = row.get('author')
        if author_username:
            author, _ = User.objects.get_or_create(username=author_username)
            row['author'] = author.pk


@admin.register(Offer)
class OfferAdmin(ImportExportModelAdmin):
    resource_class = OfferResource
    
    list_display = (
        "title",
        "author",
        "price",
        "location",
        "topic",
        "created_at",
    )
    search_fields = ("title", "author__username", "location", "topic__name")
    list_filter = ("topic", "created_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("offer", "author", "created_at")
    search_fields = ("offer__title", "author__username")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    raw_id_fields = ("offer", "author")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("chat", "author", "created_at")
    search_fields = ("chat__offer__title", "author__username", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    raw_id_fields = ("chat", "author")
