# Generated by Django 3.2 on 2021-04-12 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20210410_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.TextField(default='\\voting\\static\\voting\\IMG'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='vote',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 4, 17)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 4, 12)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voting_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='vote',
            name='winner',
            field=models.CharField(default='Победитель пока не определен. Голосование продолжается.', max_length=40),
        ),
    ]
