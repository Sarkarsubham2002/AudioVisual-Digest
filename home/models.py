from django.db import models


class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')





# Create your models here.
class details(models.Model):
    person_name = models.CharField(max_length=30)

    summary = models.TextField()

