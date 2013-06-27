from django.db import models
from django.forms import ModelForm

class Owner(models.Model):
    first_name = models.CharField(max_length=255,
                                  )
    last_name = models.CharField(max_length=255,
                                 )
    def __unicode__(self):
        return self.last_name, self.first_name

class Dog(models.Model):
    dog_name = models.CharField(max_length=255,
                                )
    owner = models.ForeignKey(Owner)
    
    def __unicode__(self):
        return self.dog_name

class OwnerForm(ModelForm):
    class Meta:
        model = Owner

class DogForm(ModelForm):
    class Meta:
        model = Dog





