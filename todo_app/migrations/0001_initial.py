# Generated by Django 4.0.4 on 2022-12-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_app',
            fields=[
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
