#!/usr/bin/python3
from django.db import models
from django.utils import timezone
from extras.models import PassEnergie, Images, Beschreibung, Video, Grundriss, Expose


def image_upload_path(instance, filename):
    return '/'.join(['images', str(instance.art), filename])

def image_upload_path_news(instance, filename):
    return '/'.join(['images', str(instance.title), filename])


class Immobilie(models.Model):
    """Realestate-object"""
    IMMOBILIEN_ART = (
        ('EFH', 'Einfamilienhaus'),
        ('WE', 'Wohnung eigennutzung'),
        ('WK', 'Wohnung kapitalanlage'),
        ('MFH', 'Mehrfamilienhaus'),
        ('GR', 'Grundstück'),
        ('GEW', 'Gewerbe'),
        ('VK', 'Verkauft'),
    )
    immobilienArt = models.CharField(max_length=3, choices=IMMOBILIEN_ART)
    title = models.CharField(max_length=200)
    objektart = models.CharField(max_length=200)
    lage = models.CharField(max_length=200)
    addresse = models.CharField(max_length=200, blank=True, null=True)
    baujahr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    grundstuecksfl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wohnfl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gewerbefl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nutzfl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mieteinnhmSoll = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mieteinnhmIst = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wheinheiten = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gwbeinheiten = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    stellpltz = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    leerstand = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    kfpreis = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    euroQuadratM = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    faktor = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    honorar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    etagen = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    anzahlZi = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hausgld = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lfzMietVertrg = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    objekbesrbng = models.ForeignKey(Beschreibung, on_delete=models.CASCADE, blank=True, null=True)
    energieAusweis = models.ForeignKey(PassEnergie, on_delete=models.CASCADE, blank=True, null=True)
    bild = models.ForeignKey(Images, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    grdriss = models.ForeignKey(Grundriss, on_delete=models.CASCADE, blank=True, null=True)
    expose = models.ForeignKey(Expose, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Leistungen(models.Model):
    LEISTUNG_ARTEN = (
        ('PE', 'Person'),
        ('VK', 'Verkaufen'),
        ('AK', 'Ankaufen'),
        ('BW', 'Bewertung'),
        ('BR', 'Beratung'),
    )
    art = models.CharField(max_length=2, choices=LEISTUNG_ARTEN)
    bild = models.ImageField(upload_to=image_upload_path, blank=True)
    text = models.TextField()


class ImmoNews(models.Model):
    """Some news out of the realestate world"""
    title = models.CharField(max_length=200)
    obererText = models.TextField(blank=True)
    bild = models.ImageField(upload_to=image_upload_path_news, blank=True)
    untererText = models.TextField(blank=True)
    linkname = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField()
    created = models.DateField(default=timezone.now)


class Contact(models.Model):
    """Contact-object"""
    vorBuero = models.BigIntegerField()
    buero = models.BigIntegerField()
    vorMobile = models.BigIntegerField()
    mobile = models.BigIntegerField()
    mail = models.EmailField()
    addresse = models.CharField(max_length=200)
    obererText = models.TextField(blank=True)
    mittlererText = models.TextField(blank=True)
    untererText = models.TextField(blank=True)