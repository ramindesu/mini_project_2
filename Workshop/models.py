from django.db import models
from Accounts.models import BaseModel , Instructor

# Create your models here.

class Workshop(BaseModel):
    title = models.CharField(max_length=60)
    address = models.TextField()
    teacher = models.ForeignKey(Instructor , on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} - Teacher: {self.teacher.name}"
    
    class Meta:
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshops'
        ordering = ['title']
        