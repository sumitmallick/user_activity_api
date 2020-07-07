from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ActivityModel, UserData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ['user', 'external_id', 'full_name', 'timezone']


class ActivityModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityModel
        fields = ['user', 'userdata', 'start_time', 'end_time']
