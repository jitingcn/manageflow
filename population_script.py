#!/usr/bin/env python
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manageflow.settings')
from django.db import IntegrityError
import django

django.setup()
from manageflow.boards.models import Board, Task
from manageflow.accounts.models import User


def populate():
    superuser = [{'username': 'alice', 'email': 'alice@example.org', 'password': 'alice123',
                  'nickname': 'alice'}]
    user = [{'username': 'oscarfolk', 'email': 'oscarfolk@example.org', 'password': 'oscarfolk123',
             'nickname': 'oscarfolk'},
            {'username': 'bootskarma', 'email': 'bootskarma@example.org', 'password': 'bootskarma123',
             'nickname': 'bootskarma'},
            {'username': 'lolatack', 'email': 'lolatack@example.org', 'password': 'lolatack123',
             'nickname': 'lolatack'}]

    board = [{'name': 'alice1', 'description': 'alice board 1', 'admin': 'alice'},
             {'name': 'alice2', 'description': 'alice board 2', 'admin': 'alice'},
             {'name': 'alice3', 'description': 'alice board 3', 'admin': 'alice'},
             {'name': 'lolatack', 'description': 'lolatack board', 'admin': 'lolatack'}]

    tasks = [{'text': 'task 1'}, {'text': 'task 2'}, {'text': 'working task'},
             {'text': 'completed task', 'complete': True}]
    try:
        for data in superuser:
            User.objects.create_superuser(data['username'], data['email'], data['password'], nickname=data['nickname'])
        for data in user:
            User.objects.create_user(data['username'], data['email'], data['password'], nickname=data['nickname'])
    except IntegrityError:
        pass
    for data in board:
        admin = User.objects.get(username=data['admin'])
        b = Board.objects.get_or_create(name=data['name'], description=data['description'], admin=admin)[0]
        if b.name == "alice1":
            for task in tasks:
                t = Task.objects.get_or_create(text=task['text'], assigned_to="alice", admin=admin, board_id=b.id)[0]
                t.complete = task.get('complete') or False
                t.save()


if __name__ == '__main__':
    populate()
