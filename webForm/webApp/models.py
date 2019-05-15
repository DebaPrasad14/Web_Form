from django.db import models

# Create your models here.

class UserField(models.Model):
    name  = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    job   = models.CharField(max_length = 100)
    upload = models.FileField(upload_to = None, max_length = 100)

    class Meta:
        db_table = "userfield"
