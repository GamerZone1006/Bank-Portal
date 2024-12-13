# Generated by Django 5.0.7 on 2024-12-12 08:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_support_alter_transaction_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAW', 'Withdraw'), ('TRANSFER', 'Transfer')], max_length=20)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2024, 12, 12, 8, 19, 22, 196702, tzinfo=datetime.timezone.utc))),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('about', models.CharField(max_length=100)),
                ('receiptent', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.user_reg')),
            ],
        ),
        migrations.DeleteModel(
            name='transaction',
        ),
    ]
