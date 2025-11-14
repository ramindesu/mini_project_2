from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    delatable = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Instructor(BaseModel):
    name = models.CharField(max_length=60)
    field = models.CharField(max_length=60)
    description = models.TextField(null= True , blank=True)

    def __str__(self):
        return f"{self.name} - {self.field}"
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'
        ordering = ['name']