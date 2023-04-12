from django.contrib import admin
from .models import Pet, PetSitter


# Register your models here.
admin.site.register(Pet)
admin.site.register(PetSitter)