# Generated by Django 3.2.5 on 2021-07-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
