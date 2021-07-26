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
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]