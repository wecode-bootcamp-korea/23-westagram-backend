# Generated by Django 3.2.5 on 2021-07-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField(null=True)),
                ('phone_number', models.CharField(max_length=60, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
