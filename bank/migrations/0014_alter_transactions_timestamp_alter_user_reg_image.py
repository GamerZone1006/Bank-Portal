# Generated by Django 5.0.7 on 2024-12-15 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0013_alter_transactions_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 13, 29, 18, 650639, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='image',
            field=models.ImageField(default='./media/User/Images/photo.jpg', null=True, upload_to='User/Images'),
        ),
    ]
