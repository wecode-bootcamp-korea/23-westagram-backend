# Generated by Django 3.2.5 on 2021-07-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_numbers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='privacy',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='introduce',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
