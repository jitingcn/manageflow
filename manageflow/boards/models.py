import uuid


from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.urls import reverse

from manageflow.accounts.models import User

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Board")
    name = models.CharField(max_length=200)

    class meta:
        ordering =('name',)
        verbose_name = "board"
        verbose_name_plural = "Boards"

    def get_absolute_url(self):
        return ('detail', (),
                {
                    'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    #board = models.ForeignKey(Board, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.text



