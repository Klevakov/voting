# Generated by Django 3.2 on 2021-04-13 11:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_auto_20210413_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 11, 21, 6, 425657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 13, 11, 21, 6, 425657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='winner',
            field=models.CharField(default='Победитель пока не определен. Голосование продолжается.', max_length=100),
        ),
    ]
