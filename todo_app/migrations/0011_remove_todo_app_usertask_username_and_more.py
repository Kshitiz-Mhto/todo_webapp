# Generated by Django 4.0.4 on 2023-01-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0010_alter_todo_app_usertask_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_app_usertask',
            name='username',
        ),
        migrations.AddField(
            model_name='todo_app_usertask',
            name='title_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='todo_app_usertask',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
