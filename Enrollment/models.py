from django.db import models
from Accounts.models import Participants , BaseModel
from Workshop.models import Workshop
# Create your models here.



class Enrollment(BaseModel):
    Workshop = models.ForeignKey(Workshop , on_delete= models.CASCADE)
    Participants = models.ForeignKey(Workshop , on_delete= models.CASCADE)
    enroll_date = models.DateField()

    def __str__(self):
        return {self.Workshop.title}
    
    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        ordering = ['enroll_date']