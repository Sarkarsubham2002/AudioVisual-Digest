from django.db import models


class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')