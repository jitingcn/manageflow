import uuid
from django.db import models
from manageflow.accounts.models import User
from django.template.defaultfilters import slugify

class Board(models.Model):
	board_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Board")
	name = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Board, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Task(models.Model):
	board = models.ForeignKey(Board, on_delete=models.CASCADE)
	admin = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()
	assigned_to = models.CharField(max_length=30)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.text)
		super(Task, self).save(*args, **kwargs)

	def __str__(self):
		return self.text

class group(models.Model):
	group_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	group_name = models.CharField(max_length=200)
	board = models.ForeignKey(Board, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.group_name)
		super(group, self).save(*args, **kwargs)

	def __str__(self):
		return self.group_name

class User_belongs_to_group(models.Model):
	group = models.ForeignKey(group, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)