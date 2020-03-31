import uuid
from django.db import models

# A really basic board model
from django.template.defaultfilters import slugify


class Board(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	description = models.TextField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Board, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Task(models.Model):
	board = models.ForeignKey(Board, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Task, self).save(*args, **kwargs)

	def __str__(self):
		return self.text


