# Generated by Django 3.2.5 on 2022-02-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='executetransitionplan_transitionhoursitem',
            field=models.FloatField(default='0.30952380952381'),
        ),
        migrations.AlterField(
            model_name='order',
            name='numtransformationweeks',
            field=models.FloatField(default='12.0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='numtransitionweeks',
            field=models.FloatField(default='12.0'),
        ),
    ]