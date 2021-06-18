from django.db import models
class PersonalInfoNew(models.Model):
    File = models.FileField(upload_to='csvs')
    activated=models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return f'File.id:{self.id}'

