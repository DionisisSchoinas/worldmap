from django.db import models
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator 
import os

# Create your models here.
class User(models.Model):
	username  = models.CharField(max_length=40)
	password  = models.CharField(max_length=40)

class Map(models.Model):
	name 	= models.CharField(max_length=40)
	image	= models.ImageField(upload_to="maps/", max_length=255, blank=True, null=True) 
	on_user = models.IntegerField()

class LandMark(models.Model):
	name		= models.CharField(max_length=100)
	description = models.CharField(max_length=10000)
	color   	= models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
	id_on_map   = models.IntegerField()
	on_map		= models.IntegerField()
	xcor		= models.FloatField()
	ycor		= models.FloatField()

@receiver(models.signals.post_delete, sender=Map)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)