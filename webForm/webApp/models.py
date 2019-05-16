from django.db import models


class UserField(models.Model):
    name  = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    job_title   = models.CharField(max_length = 100)
    resume = models.FileField(upload_to = None, max_length = 100)

    class Meta:
        db_table = "userfield"
