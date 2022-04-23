from django.db import models

# Create your models here.

class Diak(models.Model):
    oktatasi_azonosito = models.CharField(max_length=30)    
    nev = models.CharField(max_length=30)
    pontszam = models.IntegerField(max_length=3)
    Atagozat = models.BooleanField()
    Btagozat = models.BooleanField()
    Ctagozat = models.BooleanField()
    Dtagozat = models.BooleanField()
    Etagozat = models.BooleanField()
    Ftagozat = models.BooleanField()
    
    class Meta:
        verbose_name = "Diak"
        verbose_name_plural = "Diakok"
