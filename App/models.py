from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#This will be the basis of our task manage system. [WIP]
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#Related to toDoList
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Members(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text