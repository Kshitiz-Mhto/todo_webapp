# Generated by Django 4.0.4 on 2023-01-04 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0011_remove_todo_app_usertask_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_app_usertask',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='todo_app.todo_app'),
        ),
    ]