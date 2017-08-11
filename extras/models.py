from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


def image_upload_path(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


def pdf_upload_path(instance, filename):
    return '/'.join(['pdf', str(instance.name), filename])


class PassEnergie(models.Model):
    """Energiepassport-object for a realestate"""
    baujahr = models.IntegerField(blank=True, null=True)
    heizungsart = models.CharField(max_length=250, blank=True, null=True)
    befeuerungEnergietraeger = models.CharField(max_length=500, blank=True, null=True)
    energiekennwert = models.IntegerField(blank=True, null=True)
    effiziensklasse = models.CharField(max_length=10, blank=True, null=True)
    ausweisdatum = models.DateField(blank=True, null=True)
    gueltigBis = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.effiziensklasse


class Images(models.Model):
    name = models.CharField(max_length=250, default='image', help_text='Bitte nicht verändern')
    image1 = models.ImageField(upload_to=image_upload_path, blank=True, default='images/index.jpeg')
    image2 = models.ImageField(upload_to=image_upload_path, blank=True)
    image3 = models.ImageField(upload_to=image_upload_path, blank=True)
    image4 = models.ImageField(upload_to=image_upload_path, blank=True)
    image5 = models.ImageField(upload_to=image_upload_path, blank=True)
    image6 = models.ImageField(upload_to=image_upload_path, blank=True)
    image7 = models.ImageField(upload_to=image_upload_path, blank=True)
    image8 = FilerImageField(null=True, blank=True,
                           related_name="image8")
    created = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        text = self.name + str(self.id)
        return text

class Beschreibung(models.Model):
    objektbeschr = RichTextField()
    lage = RichTextField()
    ausstattung = RichTextField(blank=True)
    created = models.DateField(default=timezone.now,editable=False)


class Video(models.Model):
    name = models.CharField(max_length=250, default='video')
    video = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        text = self.name + str(self.id)
        return text

class Grundriss(models.Model):
    name = models.CharField(max_length=250, default='grundriss')
    grdriss1 = models.ImageField(upload_to=image_upload_path, blank=True)
    grdriss2 = models.ImageField(upload_to=image_upload_path, blank=True)
    grdriss3 = models.ImageField(upload_to=image_upload_path, blank=True)
    created = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        text = self.name + str(self.id)
        return text


class Expose(models.Model):
    name = models.CharField(max_length=250, default='pdf')
    expose = models.FileField(upload_to=pdf_upload_path, blank=True)
    created = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        text = self.name + str(self.id)
        return text