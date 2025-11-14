from django.db import models

# Create your models here.
class QuerySetManager(models.Manager):
    pass
    # def get_queryset(self):
    #     return super().get_queryset().filter(deleted=False)

    # def active(self):
    #     return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    delatable = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    objects = QuerySetManager()


    class Meta:
        abstract = True

