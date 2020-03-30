from django.contrib import admin
from .models import ToDoList,Item,Group,Member
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Group)
admin.site.register(Member)