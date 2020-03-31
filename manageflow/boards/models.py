import uuid

from django.db import models

# A really basic board model
class Board(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name


class Task(models.Model):
	board = models.ForeignKey(Board, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text


