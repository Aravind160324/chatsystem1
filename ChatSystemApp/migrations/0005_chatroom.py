# Generated by Django 5.0.1 on 2024-02-03 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatSystemApp', '0004_friendslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChatSystemApp.follower')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChatSystemApp.following')),
            ],
        ),
    ]
