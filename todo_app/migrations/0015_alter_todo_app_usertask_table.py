# Generated by Django 4.0.4 on 2023-01-04 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0014_alter_todo_app_usertask_title_id_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='todo_app_usertask',
            table='tasks',
        ),
    ]
