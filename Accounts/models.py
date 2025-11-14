from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    delatable = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

