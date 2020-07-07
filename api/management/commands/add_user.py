import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-u', '--username', type=str, help='Define a username prefix')
        parser.add_argument('-p', '--password', type=str, help='Define a username password')
        parser.add_argument('-f', '--file', type=str, help='Define a file to upload')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        username = kwargs['username']
        password = kwargs['password']
        admin = kwargs['admin']

        user_name = User.objects.filter(username=username)
        for i in range(total):
            if username:
                username = '{prefix}'.format(prefix=username)
            else:
                username = get_random_string()
            if admin:
                if password:
                    User.objects.create_superuser(username=username, email='', password=password)
                else:
                    User.objects.create_superuser(username=username, email='', password='123')
            else:
                if password:
                    if user_name is None:
                        User.objects.create_user(username=username, email='', password=password)
                    else:
                        print('user already exists')

                else:
                    if user_name is None:
                        User.objects.create_user(username=username, email='', password='123')
                    else:
                        print('user already exists')

