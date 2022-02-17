# Generated by Django 4.0.1 on 2022-01-14 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_column='Created:')),
                ('configmastermodifydate', models.DateTimeField(db_column='Modify Date:')),
                ('configmastername', models.CharField(blank=True, db_column='Name:', max_length=150, null=True)),
                ('configmasterdesc', models.CharField(blank=True, db_column='Description:', max_length=150, null=True)),
                ('configmasternotes', models.CharField(blank=True, db_column='Notes:', max_length=150, null=True)),
            ],
        ),
    ]