# Generated by Django 4.2.1 on 2023-06-01 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdcapp', '0003_alter_postrequestcloud_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrequestcloud',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 23, 48, 58, 974262, tzinfo=datetime.timezone.utc)),
        ),
    ]
