from django.db import models

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
    
    def __unicode__(self):
        return self.dog_name






