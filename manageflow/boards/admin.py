from django.contrib import admin
from .models import Board, Task

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['board', 'text', 'assigned_to']

admin.site.register(Board, BoardAdmin)
admin.site.register(Task)
