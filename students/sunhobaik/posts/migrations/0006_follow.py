# Generated by Django 3.2.5 on 2021-07-27 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210723_0602'),
        ('posts', '0005_auto_20210727_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='users.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='now_user', to='users.user')),
            ],
            options={
                'db_table': 'follows',
            },
        ),
    ]