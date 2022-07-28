from django.db import models

# Create your models here.

class Lesson(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(max_length=100000)
	image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	isAdvanced = models.BooleanField(default=False)
