from django.contrib import admin
from .models import PassEnergie, Images, Video, Beschreibung, Grundriss, Expose

# Register your models here.
class PassEnergieAdmin(admin.ModelAdmin):
    list_display = ('effiziensklasse', 'gueltigBis')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'id')


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'id')


class BeschreibungAdmin(admin.ModelAdmin):
    list_display = ('created', 'id')


class GrundrissAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'id')


class ExposeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'id')


admin.site.register(PassEnergie, PassEnergieAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Beschreibung, BeschreibungAdmin)
admin.site.register(Grundriss, GrundrissAdmin)
admin.site.register(Expose, ExposeAdmin)