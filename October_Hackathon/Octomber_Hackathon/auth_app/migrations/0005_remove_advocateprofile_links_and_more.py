# Generated by Django 4.1.2 on 2022-11-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_advocateprofile_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocateprofile',
            name='links',
        ),
        migrations.AddField(
            model_name='advocateprofile',
            name='twitter_link',
            field=models.URLField(default='https://twitter.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advocateprofile',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
