from django.contrib import admin

from .models import UserActivity, ResizeImage


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ["slug", "image", "result", "created_at"]

@admin.register(ResizeImage)
class ResizeImageAdmin(admin.ModelAdmin):
    list_display = ['image' , 'created_at']