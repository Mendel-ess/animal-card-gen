from django.db import models

# Create your models here.

class Card(models.Model):
    animal_name = models.CharField(max_length=200)
    animal_type = models.CharField(max_length=200)
    animal_contact = models.CharField(max_length=200)
    animal_image_url = models.CharField(max_length=500)