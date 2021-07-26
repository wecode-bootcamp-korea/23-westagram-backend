# Generated by Django 3.2.5 on 2021-07-23 08:20

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
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=45)),
                ('age', models.PositiveIntegerField(max_length=3)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]