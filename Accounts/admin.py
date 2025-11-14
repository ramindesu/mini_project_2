from django.contrib import admin
from .models import Participants , Instructor
# Register your models here.

@admin.register(Participants)
class AdminParticipants(admin.ModelAdmin):
    pass

@admin.register(Instructor)
class AdminInstructor(admin.ModelAdmin):
    pass

