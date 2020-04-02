from django.contrib import admin
from .models import Board, Task, group, User_belongs_to_group

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(group)
admin.site.register(User_belongs_to_group)