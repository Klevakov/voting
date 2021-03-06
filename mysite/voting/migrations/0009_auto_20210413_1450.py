# Generated by Django 3.2 on 2021-04-13 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0008_auto_20210413_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 11, 50, 29, 540849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 13, 11, 50, 29, 540849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='votetoperson',
            name='moment_of_last_voice',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 14, 50, 29, 540849)),
        ),
    ]
