from django.db import models

# Create your models here.
class UploadedPersonalDetails(models.Model):
    
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    PhoneNumber = models.CharField(max_length=11)
    EmailAddress = models.CharField(max_length=255, unique=True)
    RoomNumber = models.CharField(max_length=5)
    SubjectsTaught =models.CharField(max_length=205)
    Photo =models.CharField(max_length=200)
    def __str__(self):
        return f'id:{self.id}'