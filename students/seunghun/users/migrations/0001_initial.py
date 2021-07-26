# Generated by Django 3.2.5 on 2021-07-23 06:07

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
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=200, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('nickname', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]