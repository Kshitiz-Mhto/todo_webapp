# Generated by Django 4.0.4 on 2019-11-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_todo_app_usertask_userdata_delete_todo_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userdata',
        ),
        migrations.AddField(
            model_name='todo_app_usertask',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]