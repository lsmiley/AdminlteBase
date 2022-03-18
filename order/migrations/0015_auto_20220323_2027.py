# Generated by Django 3.2.5 on 2022-03-24 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20220323_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='CustomerName',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='SalesContactEmail',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='SalesContactName',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='TranStartDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
