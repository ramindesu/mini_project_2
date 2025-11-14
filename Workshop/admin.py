from django.contrib import admin
from .models import Workshop
# Register your models here.

@admin.register(Workshop)
class AdminWorkshop:
    pass



