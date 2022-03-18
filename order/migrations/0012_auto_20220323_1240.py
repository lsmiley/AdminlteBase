# Generated by Django 3.2.5 on 2022-03-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20220323_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='addl_Services',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='combined_Svcs',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='components',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='custom_Optns',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='first_line_mgr_steadystate_hrs',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='second_line_mgr_steadystate_hrs',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_steadystate_hours',
            field=models.FloatField(default='0.0'),
        ),
    ]
