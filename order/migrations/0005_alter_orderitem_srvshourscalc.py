# Generated by Django 3.2.5 on 2022-03-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_prodcomponent9_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='srvshourscalc',
            field=models.FloatField(default=0.0),
        ),
    ]
