# Generated by Django 3.2.5 on 2022-05-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testquestionnaire', '0003_auto_20220511_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestionnaire',
            name='CustomerStatus',
            field=models.CharField(choices=[('---Select one ---', '---Select one ---'), ('New Customer', 'New Customer'), ('Added scope Existing ESS Customer', 'Added scope Existing ESS Customer'), ('Customer has other services from MSS', 'Customer has other services from MSS'), ('Direct Deal - 6950-38N ', 'Direct Deal - 6950-38N '), ('Revenue share - 6950 -38L ( IBM Consulting)', 'Revenue share - 6950 -38L ( IBM Consulting)')], default='Select-One', max_length=150),
        ),
        migrations.AlterField(
            model_name='testquestionnaire',
            name='Revenue_Structure_Select',
            field=models.CharField(choices=[('---Select one ---', '---Select one ---'), ('Direct Deal - 6950-38N ', 'Direct Deal - 6950-38N '), ('Revenue share - 6950 -38L ( IBM Consulting)', 'Revenue share - 6950 -38L ( IBM Consulting)')], default='Select-One', max_length=150),
        ),
    ]
