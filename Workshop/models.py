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


 
class Tag(BaseModel):
    title = models.CharField(max_length=60)
    Workshop = models.ManyToManyField(Workshop,through="TagWorkshopCustomTable")

class TagWorkshopCustomTable(BaseModel):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    Workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)
    test_field = models.CharField(max_length=2)
