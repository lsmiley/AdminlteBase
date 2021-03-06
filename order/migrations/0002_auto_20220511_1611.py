# Generated by Django 3.2.5 on 2022-05-11 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='AIX',
        ),
        migrations.RemoveField(
            model_name='order',
            name='AntiVirusMalware',
        ),
        migrations.RemoveField(
            model_name='order',
            name='BigFix_Patching_Scanning',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Citrix',
        ),
        migrations.RemoveField(
            model_name='order',
            name='CustomerName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='CustomerStatus',
        ),
        migrations.RemoveField(
            model_name='order',
            name='DLP_on_Servers',
        ),
        migrations.RemoveField(
            model_name='order',
            name='DLP_on_Workstations',
        ),
        migrations.RemoveField(
            model_name='order',
            name='EmsServiceRequested',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Encryption_on_Servers',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Encryption_on_Workstations',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Environment_and_Platforms_Note',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Firewall_on_Servers',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Firewall_on_Workstations',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Firm_Price_or_NBIE',
        ),
        migrations.RemoveField(
            model_name='order',
            name='HIPs_on_Servers',
        ),
        migrations.RemoveField(
            model_name='order',
            name='HIPs_on_Workstations',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Integrity_Monitoring',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Linux',
        ),
        migrations.RemoveField(
            model_name='order',
            name='NAS_Storage',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Other_Features_or_Platforms',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Other_Features_or_Platforms_Note',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Questionaire_num_consoles',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Questionaire_num_ipaddress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Questionaire_num_server',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Questionaire_num_total_endpoints',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Questionaire_num_workstation',
        ),
        migrations.RemoveField(
            model_name='order',
            name='RequesterEmail',
        ),
        migrations.RemoveField(
            model_name='order',
            name='RequesterFirstName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='RequesterLastName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='RequesterRole',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Restricted_Delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Restricted_Delivery_Explanation',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Revenue_Structure_Cost_Explain',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Revenue_Structure_Select',
        ),
        migrations.RemoveField(
            model_name='order',
            name='SalesContactEmail',
        ),
        migrations.RemoveField(
            model_name='order',
            name='SalesContactName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Service_Delivery_Requirements',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Solution_Design',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Solution_Owner',
        ),
        migrations.RemoveField(
            model_name='order',
            name='TranStartDate',
        ),
        migrations.RemoveField(
            model_name='order',
            name='URL_Filtering',
        ),
        migrations.RemoveField(
            model_name='order',
            name='VDI',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Windows',
        ),
        migrations.RemoveField(
            model_name='order',
            name='prodcomponent1_wkstn',
        ),
    ]
