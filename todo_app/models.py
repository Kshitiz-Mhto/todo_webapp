from django.db import models
from django import forms
from django.contrib.auth import authenticate

# Create your models here.

class Todo_app(models.Model):
    fullname = models.CharField(max_length=50, blank=False,  null=False)
    username = models.CharField(max_length=20, primary_key=True)
    email = models.CharField(max_length=40, blank=False,  null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    class Meta:
        db_table= 'users'
    def __init__(self, fullname, username, email, password):
        super(Todo_app, self).__init__(fullname, username, email,password)
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password

class Todo_app_userTask(models.Model):
    username = models.CharField(max_length=20)
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    detail = models.CharField(max_length=100, blank=False, null=False)
    is_complete = models.BooleanField(default=False)
    class Meta:
        db_table= 'usertask'
    def __init__(self,username,id,title,detail,is_complete):
        super(Todo_app_userTask, self).__init__(username,id,title,detail,is_complete)
        self.id = title_id
        self.username = username
        self.detail = detail
        self.is_complete = is_complete