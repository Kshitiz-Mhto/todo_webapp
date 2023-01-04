from django.db import models
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
    user = models.ForeignKey(Todo_app, on_delete=models.CASCADE, default="")
    title_id = models.IntegerField()
    title = models.CharField(max_length=50, blank=False, null=False)
    detail = models.CharField(max_length=100, blank=False, null=False)
    is_complete = models.BooleanField(default=False)
    
    class Meta:
        db_table= 'tasks'
    def __init__(self,title_id,title,detail,is_complete):
        super(Todo_app_userTask, self).__init__(self,title_id,title,detail,is_complete)
        self.title_id = title_id
        self.title = title
        self.detail = detail
        self.is_complete = is_complete
