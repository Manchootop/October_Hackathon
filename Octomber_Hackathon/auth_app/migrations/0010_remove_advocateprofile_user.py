# Generated by Django 4.1.2 on 2022-11-05 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0009_advocateprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocateprofile',
            name='user',
        ),
    ]
