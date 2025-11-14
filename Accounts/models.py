from django.db import models
from config.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.


class Instructor(BaseModel):
    name = models.CharField(max_length=60)
    field = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.field}"
    
    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"
        ordering = ["name"]
        db_table = 'Instructor'


class Participants(User):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} - {self.last_name}"

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"
        ordering = ["name"]

