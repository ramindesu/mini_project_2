from django.contrib import admin
from .models import Enrollment
# Register your models here.

@admin.register(Enrollment)
class AdminEnrollment(admin.ModelAdmin):
    pass
