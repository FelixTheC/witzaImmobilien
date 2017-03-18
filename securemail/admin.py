from django.contrib import admin
from .models import SaveContact

class SaveContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'gesendetAm')

admin.site.register(SaveContact, SaveContactAdmin)