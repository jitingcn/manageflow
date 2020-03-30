from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class board(models.Model):
    name= models.CharField(max_length=200)
    description= models.TextField()
    user = models.oneToOneField(User, on_delete=models.CASCADE)

    #save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.acronym)
        super(board, self).save(*args, **kwargs)

    #delete

    def __str__(self):
        return self.name





