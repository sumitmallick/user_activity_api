from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=25, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name


class ActivityModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.userdata.full_name+self.start_time
