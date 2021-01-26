from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Photo(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="instaimg")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(290, 290)])
# Create your models here.
