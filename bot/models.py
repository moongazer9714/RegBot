from django.db import models

# Create your models here.


class UserInformation(models.Model):
    user_id = models.BigIntegerField(null=True, blank=True)
    region = models.CharField(max_length=256, null=True)
    full_name = models.CharField(max_length=256, null=True)
    birthday = models.CharField(max_length=256, null=True)
    location = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=256, null=True)
    education = models.CharField(max_length=256, null=True)
    project_name = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    file = models.FileField(null=True)

    def __str__(self):
        return self.full_name


class Log(models.Model):
    user_id = models.BigIntegerField()
    state = models.JSONField()