# Generated by Django 4.2.1 on 2023-09-22 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djbackend', '0020_remove_work_exp_people_alter_work_exp_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_exp',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2023, 9, 22, 21, 58, 53, 426133)),
        ),
        migrations.AlterField(
            model_name='work_exp',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2023, 9, 22, 21, 58, 53, 426133)),
        ),
    ]