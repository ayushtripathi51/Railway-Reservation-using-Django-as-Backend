# Generated by Django 2.0 on 2018-01-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Railapp', '0006_auto_20180109_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_week_schedule',
            name='friday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='train_week_schedule',
            name='monday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='train_week_schedule',
            name='saturday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='train_week_schedule',
            name='sunday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='train_week_schedule',
            name='thursday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='train_week_schedule',
            name='tuesday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='train_week_schedule',
            name='wednesday',
            field=models.BooleanField(default=True),
        ),
    ]
