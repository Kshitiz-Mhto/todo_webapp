# Generated by Django 3.2.12 on 2023-01-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userTask',
            fields=[
                ('title_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usertask',
            },
        ),
    ]
