# Generated by Django 4.0.4 on 2023-01-04 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0012_todo_app_usertask_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='todo_app_usertask',
            table='usertaski',
        ),
    ]