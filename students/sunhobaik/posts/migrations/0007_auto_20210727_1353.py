# Generated by Django 3.2.5 on 2021-07-27 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210723_0602'),
        ('posts', '0006_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='following_user',
        ),
        migrations.AddField(
            model_name='follow',
            name='follow_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to='users.user'),
        ),
    ]
