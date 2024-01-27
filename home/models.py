from django.db import models
from django.conf import settings


class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')


class Output_content(models.Model):
    user = models.CharField(max_length=50)
    output_sum = models.TextField()
    title = models.CharField(max_length=255, default='Your Default Value')
    
    objects = models.Manager()


