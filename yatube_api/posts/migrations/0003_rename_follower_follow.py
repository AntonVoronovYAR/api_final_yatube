# Generated by Django 3.2.16 on 2023-03-14 16:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20230314_1251'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follower',
            new_name='Follow',
        ),
    ]
