import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from api.models import *


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, help='Define a file to upload')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        if file_path:
            with open(file_path) as f:
                json_data = json.load(f)

                for data in json_data['members']:
                    user_real_id = data['id']
                    real_name = data['real_name']
                    timezone = data['tz']
                    user = User.objects.get(username='admin')

                    if user_real_id and real_name and timezone:
                        user_data = UserData.objects.create(user=user, external_id=user_real_id, full_name=real_name, timezone=timezone)

                    for activity in data['activity_periods']:
                        start_time = activity['start_time']
                        end_time = activity['end_time']
                        print(user_real_id, real_name, timezone, start_time, end_time)
                        if user_real_id and real_name and timezone:
                            ActivityModel(user=user, userdata=user_data, start_time=start_time, end_time=end_time).save()
