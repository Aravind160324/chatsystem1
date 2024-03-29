# Generated by Django 5.0.1 on 2024-02-03 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatSystemApp', '0003_delete_friendslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChatSystemApp.follower')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChatSystemApp.following')),
            ],
        ),
    ]
