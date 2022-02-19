from django.contrib import admin

from .models import ContactModel, HomeBannerModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(HomeBannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'collection']
    list_display_links = ['id', 'title', 'collection']
    search_fields = ['collection']
