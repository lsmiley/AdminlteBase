# Generated by Django 3.2.5 on 2022-06-28 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeritem',
            name='sizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizer_items', to='sizer.sizer'),
        ),
    ]
