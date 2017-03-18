#!/usr/bin/python3
from django.contrib import admin
from .models import Immobilie, ImmoNews, Contact, Leistungen


class ImmobilieAdmin(admin.ModelAdmin):
    list_display = ('title', 'immobilienArt', 'lage')


admin.site.register(Immobilie, ImmobilieAdmin)


class ImmoNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created')

admin.site.register(ImmoNews, ImmoNewsAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('buero', 'mobile', 'addresse', 'mail')

admin.site.register(Contact, ContactAdmin)


class LeistungAdmin(admin.ModelAdmin):
    list_display = ('art', 'id')

admin.site.register(Leistungen, LeistungAdmin)
