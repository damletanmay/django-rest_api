# Generated by Django 3.2.1 on 2021-05-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_booking_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
