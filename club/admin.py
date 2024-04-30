from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post, Contact
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "like", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")
    list_filter = ("name", "email")
    search_fields = ("name", "email", "message")


admin.site.register(Contact, ContactAdmin)