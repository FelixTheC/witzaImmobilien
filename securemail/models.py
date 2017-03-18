from django.db import models
from django.utils import timezone

# Create your models here.
class SaveContact(models.Model):
    """saving mail contacts"""
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    gesendetAm = models.DateField(default=timezone.now)

    def __self__(self):
        return self.name