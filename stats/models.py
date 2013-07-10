from django.db import models
from django.forms import ModelForm
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Owner(models.Model):
    first_name = models.CharField(max_length=255,
                                  )
    last_name = models.CharField(max_length=255,
                                 )
    def __unicode__(self):
        return self.last_name

class Dog(models.Model):
    dog_name = models.CharField(max_length=255,
                                )
    owner = models.ForeignKey(Owner)    
    photo = models.ImageField(upload_to='dogs',
                              blank=True,
                              null=True)
    ptoto_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFit(150, 150)],
                                     format='JPEG',
                                     options={'quality':60})

    def __unicode__(self):
        return self.dog_name

class OwnerForm(ModelForm):
    class Meta:
        model = Owner

class DogForm(ModelForm):
    class Meta:
        model = Dog





