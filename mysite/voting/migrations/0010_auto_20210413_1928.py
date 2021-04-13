# Generated by Django 3.2 on 2021-04-13 16:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0009_auto_20210413_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 16, 28, 10, 784753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 13, 16, 28, 10, 784753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='winner',
            field=models.CharField(default='Победитель пока не определен. Голосование продолжается.', max_length=150),
        ),
        migrations.AlterField(
            model_name='votetoperson',
            name='moment_of_last_voice',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 19, 28, 10, 785750)),
        ),
    ]
