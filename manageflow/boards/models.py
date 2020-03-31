import uuid

from manageflow.accounts.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    STATUSES = (
        ('to-do', ('To Do')),
        ('in_progress', ('In Progress')),
        ('blocked', ('Blocked')),
        ('done', ('Done')),
        ('dismissed', ('Dismissed'))
    )

    title = models.CharField( max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, related_name='tasks_assigned', verbose_name=('assigned to'),
                                   on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(("state"), max_length=20, choices=STATUSES, default='to-do')
    created_by = models.ForeignKey(User, related_name='users_created', verbose_name=('created by'),
                                   on_delete=models.SET_NULL, null=True)

class Board(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    item_description = models.CharField(("description"), max_length=200)
    is_done = models.BooleanField(("done?"), default=False)

    def __str__(self):
        return self.item_description