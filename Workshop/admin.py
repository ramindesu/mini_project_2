from django.contrib import admin
from .models import Workshop , Tag
# Register your models here.

@admin.register(Workshop)
class AdminWorkshop(admin.ModelAdmin):
    pass



@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass

